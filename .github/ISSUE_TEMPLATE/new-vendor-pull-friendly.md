---
name: Add/Update Vendor (Pull Request Friendly)
about: Use this template to create a pull request friendly issue.
  
---

  **Is this issue to add a new vendor, or update an existing entry?**
  (e.g. new)

  **How to use**
- **name:** Use the vendors name 
- **url:** Use the vendors public website
- **base_pricing:** Use the vendors cheapest available price suitable for teams/companies.  A plan limited to less than 10 users may not be suited for companies.
- **sso_pricingr:** Use the vendors cheapest price that includes SSO. 
- **footnotes:** If you need to clarify pricing for SSO, please add a footnote.  This is done by adding a `[^vendor]` to the appropriates line end. Describe the footnotes content in this line
- **pricing_source:** Add a link or a note to where you got the pricing from. 
- **updated_at:** yyyy-mm-dd of the day you filed this. 
  
``` 
  - name: {Vendor Name}
    url: {https://www.example.com}
    base_pricing: $9 per u/m
    sso_pricing: $19 per u/m [^vendor]
    footnotes: "[^vendor]: Describe the SSO pricing if appplicable.  Remove if not neccessary." 
    pricing_source: https://www.example.com/pricing
    updated_at: 2019-12-21 
```
