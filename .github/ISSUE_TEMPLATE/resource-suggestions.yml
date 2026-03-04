name: Resource Suggestion
description: Suggest adding or updating a tool, link, blog, cheat sheet, one-liner, etc.
title: "[Resource] Short descriptive title"
labels: ["resource", "enhancement"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for suggesting a resource! Please fill out as much as possible.

  - type: input
    id: name
    attributes:
      label: Resource Name
      description: Name of the tool, blog, list, one-liner collection, etc.
      placeholder: e.g., "nmap", "PayloadsAllTheThings", "Shell One-liner: Find large files"
    validations:
      required: true

  - type: input
    id: url
    attributes:
      label: URL / Location
      description: Direct link (or file path if already in repo)
      placeholder: https://example.com/tool or ./shell-utils/one-liners/find-large-files.md
    validations:
      required: true

  - type: dropdown
    id: category
    attributes:
      label: Which section/category does this belong to?
      options:
        - CLI Tools
        - GUI Tools
        - Web Tools
        - Systems & Services
        - Networks
        - Containers & Orchestration
        - Manuals / Howtos / Tutorials
        - Inspiring Lists
        - Blogs / Podcasts / Videos
        - Hacking / Penetration Testing
        - Daily Knowledge / News
        - Cheat Sheets
        - Shell One-liners / Tricks / Functions
        - Other (please specify below)
      default: 0
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: Description & Why Include It
      description: Brief summary + why it's valuable / unique / up-to-date.
      placeholder: "nmap is the de facto network scanner; still actively maintained in 2026."
    validations:
      required: true

  - type: input
    id: tags
    attributes:
      label: Suggested Tags / Keywords
      description: Comma-separated (helps future search/tagging)
      placeholder: nmap, scanning, network, cli

  - type: checkboxes
    id: terms
    attributes:
      label: Checklist
      options:
        - label: I have searched existing resources / issues to avoid duplicates
          required: true
        - label: The resource is legal, ethical, and publicly available
          required: true
