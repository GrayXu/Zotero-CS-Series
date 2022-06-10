# Zotero-CS-Series

Zotero won't auto-generate an abbreviation like "OSDI", so this script is for adding such pub abbreviations in `series` based other metadata in Zotero.  

So that you can [use `series` for zotfile wildcards](https://github.com/jlegewie/zotfile/issues/173)

note: the [mapping](https://github.com/GrayXu/Zotero-CS-Series/blob/main/set_series.py#L13) is only for my usage.

# Usage

1. get your `library_id` and `api_key`(w/ r+w permissions) from Zotero websites
2. backup your library
3. `pip install pyzotero tqdm`
4. run codes

# Todo

- rules for arXiv
- trans can't be abbreviated like conf?
