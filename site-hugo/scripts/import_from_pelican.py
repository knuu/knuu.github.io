from __future__ import annotations

import json
import re
import shutil
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "content"
TARGET_ROOT = ROOT / "site-hugo" / "content"
DATA_ROOT = ROOT / "site-hugo" / "data"

TAG_MAP = OrderedDict(
    [
        ("論文メモ", "paper-memo"),
        ("日記", "diary"),
        ("アルゴリズム", "algorithm"),
        ("スクレイピング", "scraping"),
        ("統計", "statistics"),
        ("聴講録", "conf_notes"),
        ("機械学習", "machine_learning"),
        ("ランキング学習", "learning_to_rank"),
        ("情報検索", "information_retrieval"),
        ("競技プログラミング", "competitive_programming"),
    ]
)

PAGE_WEIGHTS = {
    "about-me": 1,
    "ml-dm-ai_jp_papers": 2,
}

META_PATTERN = re.compile(r"^(?P<key>[A-Za-z][A-Za-z0-9_ ]+):\s*(?P<value>.*)$")
GIST_PATTERN = re.compile(r"\[gist:id=([A-Za-z0-9]+)\]")
AMAZON_IFRAME_PATTERN = re.compile(
    r'<iframe[^>]+src="(?P<src>(?:https?:)?//rcm-fe\.amazon-adsystem\.com[^"]+)"[^>]*>\s*</iframe>',
    re.IGNORECASE | re.DOTALL,
)
DATETIME_PATTERN = re.compile(
    r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})(?:\s+(?P<hour>\d{1,2}):(?P<minute>\d{2}))?$"
)


def reset_targets() -> None:
    for directory in [
        TARGET_ROOT / "posts",
        TARGET_ROOT / "pages",
        TARGET_ROOT / "tags",
        TARGET_ROOT / "categories",
        TARGET_ROOT / "authors",
    ]:
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True, exist_ok=True)


def parse_pelican_file(path: Path) -> tuple[dict[str, str], str]:
    metadata: dict[str, str] = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    body_start = 0
    for index, line in enumerate(lines):
        if not line.strip():
            body_start = index + 1
            break
        match = META_PATTERN.match(line)
        if not match:
            body_start = index
            break
        metadata[match.group("key").strip().lower().replace(" ", "_")] = match.group("value").strip()
    body = "\n".join(lines[body_start:]).strip() + "\n"
    return metadata, transform_body(body)


def slugify_tag(raw_tag: str) -> str:
    normalized = raw_tag.strip()
    if normalized in TAG_MAP:
        return TAG_MAP[normalized]
    return re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")


def transform_body(body: str) -> str:
    body = body.replace("{static}/images/", "/images/")
    body = AMAZON_IFRAME_PATTERN.sub("", body)
    body = GIST_PATTERN.sub(r'{{< gist "\1" >}}', body)
    return body


def normalize_datetime(value: str) -> str:
    match = DATETIME_PATTERN.match(value.strip())
    if not match:
        return value
    if match.group("hour") is None:
        return f'{match.group("year")}-{match.group("month")}-{match.group("day")}'
    return (
        f'{match.group("year")}-{match.group("month")}-{match.group("day")}T'
        f'{int(match.group("hour")):02d}:{match.group("minute")}:00+09:00'
    )


def toml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def toml_array(values: list[str]) -> str:
    return "[" + ", ".join(toml_string(value) for value in values) + "]"


def write_content(target: Path, metadata: dict[str, str], body: str, *, kind: str) -> dict[str, str]:
    front_matter: list[str] = ["+++"]
    front_matter.append(f'title = {toml_string(metadata["title"])}')
    if "date" in metadata:
        front_matter.append(f'date = {toml_string(normalize_datetime(metadata["date"]))}')
    if "modified" in metadata:
        front_matter.append(f'lastmod = {toml_string(normalize_datetime(metadata["modified"]))}')
    if "slug" in metadata:
        front_matter.append(f'slug = {toml_string(metadata["slug"])}')
        slug = metadata["slug"]
        if kind == "post":
            front_matter.append(f'url = {toml_string(f"/{slug}.html")}')
        else:
            front_matter.append(f'url = {toml_string(f"/pages/{slug}.html")}')
    if "summary" in metadata:
        front_matter.append(f'summary = {toml_string(metadata["summary"])}')

    exported_tags: dict[str, str] = {}
    tags_raw = metadata.get("tags", "")
    if tags_raw:
        source_tags = [tag.strip() for tag in tags_raw.split(",") if tag.strip()]
        target_tags = [slugify_tag(tag) for tag in source_tags]
        front_matter.append(f"tags = {toml_array(target_tags)}")
        exported_tags.update(dict(zip(target_tags, source_tags)))

    if kind == "post":
        front_matter.append('categories = ["blog"]')
        front_matter.append('authors = ["knuu"]')
    else:
        slug = metadata.get("slug")
        if slug in PAGE_WEIGHTS:
            front_matter.append(f"weight = {PAGE_WEIGHTS[slug]}")

    front_matter.append("+++")
    target.write_text("\n".join(front_matter) + "\n\n" + body, encoding="utf-8")
    return exported_tags


def write_tag_labels(tag_labels: dict[str, str]) -> None:
    output = DATA_ROOT / "tag_labels.toml"
    lines = [f"{key} = {toml_string(tag_labels[key])}" for key in sorted(tag_labels)]
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_term_bundle(base_dir: Path, term: str, title: str, url: str) -> None:
    bundle_dir = base_dir / term
    bundle_dir.mkdir(parents=True, exist_ok=True)
    (bundle_dir / "_index.md").write_text(
        "\n".join(
            [
                "+++",
                f"title = {toml_string(title)}",
                f"url = {toml_string(url)}",
                "+++",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_taxonomy_terms(tag_labels: dict[str, str]) -> None:
    for slug, label in sorted(tag_labels.items()):
        write_term_bundle(TARGET_ROOT / "tags", slug, label, f"/tag/{slug}.html")
    write_term_bundle(TARGET_ROOT / "categories", "blog", "blog", "/category/blog.html")
    write_term_bundle(TARGET_ROOT / "authors", "knuu", "knuu", "/author/knuu.html")


def main() -> None:
    reset_targets()
    tag_labels: dict[str, str] = {}

    for source in sorted((SOURCE_ROOT / "blog").glob("*.md")):
        metadata, body = parse_pelican_file(source)
        target = TARGET_ROOT / "posts" / source.name
        tag_labels.update(write_content(target, metadata, body, kind="post"))

    for source in sorted((SOURCE_ROOT / "pages").glob("*.md")):
        metadata, body = parse_pelican_file(source)
        target = TARGET_ROOT / "pages" / source.name
        tag_labels.update(write_content(target, metadata, body, kind="page"))

    write_tag_labels(tag_labels)
    write_taxonomy_terms(tag_labels)


if __name__ == "__main__":
    main()
