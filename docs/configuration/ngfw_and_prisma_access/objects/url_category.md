# URL Category

| | |
|---|---|
| **Accessor** | `scm.url_category` |
| **Class** | `UrlCategory` |
| **Endpoint** | `/config/objects/v1/url-categories` |
| **YAML key** | `url_categories` |

## Examples

```python
# List
categories = scm.url_category.list(folder="Prisma Access")

# Get by name
cat = scm.url_category.get("blocked-sites", folder="Prisma Access")

# Create — custom URL list
scm.url_category.create({
    "name": "blocked-sites",
    "folder": "Prisma Access",
    "type": "URL List",
    "list": ["badsite.com", "malware.example.org"],
    "description": "Manually blocked sites",
})

# Create — category match (references built-in categories)
scm.url_category.create({
    "name": "social-media-override",
    "folder": "Prisma Access",
    "type": "Category Match",
    "match": ["social-networking", "personal-sites-and-blogs"],
})

# Update by name
scm.url_category.update_by_name("blocked-sites", folder="Prisma Access",
                                 list=["badsite.com", "malware.example.org", "phish.example.net"])

# Delete by name
scm.url_category.delete_by_name("blocked-sites", folder="Prisma Access")

# Bulk from YAML
scm.url_category.create_from_yaml("tests/data/url_categories.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
url_categories:
  - name: blocked-sites
    type: URL List
    list:
      - badsite.com
      - malware.example.org
    description: Manually blocked sites

  - name: social-media-override
    type: Category Match
    match:
      - social-networking
      - personal-sites-and-blogs
```
