# NT-SDF Research - CKAN vs NADA (UX Perspective)

## Task
Run a review comparing [NADA](https://microdata.worldbank.org/home) to [CKAN](https://datasets.edge.durban/dataset/)

### Purpose
To determine which platform is more suited for the NT-SDF metadata catalog project from a user experience perspective.
A truly intuitive and engaging system for the browsability of data, datasets, metadata and associated assets is a difficult nut to crack as evidenced by the range of data management and cataloging tools out there. 
Over the years we have come across a large range of systems, all of which have a very similar look and feel. One could assume that his has become standard because users like this way of browsing but our research and engagement over the last 8 years tells us that this may be more a case of emulating the "thing" that came before than responding to user needs. 
This presents an opportunity to disrupt how government workers, researchers and the public (and the full range of possible stakeholders) find, engage and interact with data and metadata.

### Considerations
Our proposed system has to address a number of user requirements which will affect our final choice of platform.
- Is it intuitive and easy to use?
- Is it easy to maintain?
- Is it easy to integrate with other systems?
- Is it easy to customize?
- Can the user create custon metadata objects? (specific project requirement)
- Can it be made engaging for portal visitors?

### Requirements
- A review of the two platforms
- A comparison of the two platforms using a custom rubric
- A recommendation for the best platform for the NT-SDF metadata catalog project

### Methodology
1. Select case study examples to examine:
  - Our CKAN exemplar: [EDGE Data Portal](https://datasets.edge.durban/dataset/) was used to test CKAN
  - Our NADA exemplar: [World Bank Metadata Libary](https://microdata.worldbank.org/home), [DataFirst](https://www.datafirst.uct.ac.za/dataportal/index.php/catalog) and [Demo NADA Catalog](https://nada-demo.ihsn.org) were used to test NADA
2. Understand user flows - how easy/difficult is it to get straight to useable data/resources?
  - Screengrabs were taken of the portals in question and the flows plus features were noted in [this Figjam document](https://www.figma.com/board/CpYG38S9cG5lOuRSOIxU7w/NT---Metadata-Portal--User-Journeys---Wireframes-?node-id=76-554&t=6M2DscstwEdsHJNR-1)
3. What features and functionality exist on both OR are unique to one system that are relevant to this work?
  - This review was done as part of the user flow exercise described above
4. Compare systems from a user experience perspective using [this custom scoring rubric template for data portals](https://docs.google.com/spreadsheets/d/1bmh3BqSX8lLmW6CLQIUdYufXuO7OFCKEIuiS87EanZQ/edit?usp=drive_link) created by OCL + Claude

---

## Review Results

### Caveat
*It is important to note that the results above are based on what currently exists and doesn't take into consideration what is possible but not yet implemented.*
*These results contain some recommendations which, if adopted, will likely require custom build time.*

### User Flows
Looking at the [user flows](https://www.figma.com/board/CpYG38S9cG5lOuRSOIxU7w/NT---Metadata-Portal--User-Journeys---Wireframes-?node-id=76-554&t=6M2DscstwEdsHJNR-1) we were able to understand how a user might arrive at a landing page and then navigate into a metadata object or dataset. 
We were also able to appraise what that experience would be like if a user was directed straight to resource/download dataset.
We found the following:

---

**[DataFirst](https://www.datafirst.uct.ac.za/dataportal/index.php/catalog)** 
Has a landing page which can send the user either directly to the catalog or can send them on a gradutaed journey through an explainer first.
Review:
- This was the longest journey and while it did offer a direct route to data, that route was slightly obscured and the longer journey seems to be prioritised via attractive story-type cards with imagery 
- The longer journey goes some way to making the subject matter more understandable to a wider audience but it requires numerous clicks to get to the downloadable and once you are at the final point, you are very much in a typical data catalog space
- The portal is attractive with imagery and blog entries but it is clear that this requires a fair amount of curation which the NT-SDF team have explicitly stated they do not have capacity to handle

Takeaways:
We aren't able to add curation heavy aspects to our portal but what can we learn from DataFirst?
- Provide multiple routes aimed at different use types that get them to our desired end point/s
- Loads of good practices to bring into this work:
  - Narrative driven explainers
  - Modern search and filter
  - Allowing users to search by object OR resource
  - On screen trust analytics - Pages views + Downloads
  - Guided (when in the resource view) scrolling with a side nav to orientate you
  - Citations section
- Some things to look out for:
  - Don't make users work to get to the download button
  - Don't collect MdOs by internal reporting themes, cluster how users would search for resources

---

**[World Bank Metadata Libary](https://microdata.worldbank.org/home)** and **[Demo NADA Catalog](https://nada-demo.ihsn.org)**
Gets users to the usable data/resources relatively quickly.
Review:
- There are attractive story cards but skips the narrative explainer detailed in the DataFirst example
- Reduced level of curation compared to DataFirst

Takeaways:
- The two examples grouped together are very similar but styled differently showing there is decent flexibility with the NADA UI
- Metadata Object cards are clear and well presented 
- Some things to look out for:
  - Search results area needs some work - baggy, cryptic
  - NADA has a quirck in that the landing page can look similar to the catalog but different enough to create confusion, see the Demo NADA Catalog - This was observed across a few other exemplars - don't create confusion for the users
  - The portals both feel bigger than they are, be sure to orientate our users better when on a page or in a section
  - Useful to note that while NADA does not have a native template builder it is compatibile with the Worldbank Tempate Editor (discussed in detail in the "Specific User Needs" section)

---

[CKAN - EDGE Data Portal](https://datasets.edge.durban/dataset/)
Gets users to the usable data/resources relatively quickly.
Review:
- We had previously worked in the CKAN page builder space (used to build landing pages and about pages etc) before and found it limiting. CKAN does however have powerful Portal JS compatability that offers broad flexibility when it comes to the UI and UX of the pages around the data portal
- CKAN is an early pioneer in the space and therefore looks and behaves like many other data managment and catalog systems as many were modelled on it. This makes the tech feel dated and out the box, it does not reflect best UX practices.

Takeaways:
- CKAN is very sturdy, secure and has a maintenance team
- It handles user roles and assignments well
- It compartmentalises thematic data well - groups and orgs etc
- CKAN was quite simple to integrate into other systems and structures
Some things to look out for:
- The ingestion UI can feel cryptic
- The presentation of data and metadata is a wall of text - not easy to read or ingest or browse
- The design flexibility specifcially of the data browsing space is very limited, we have reached the outer limits there, any more customisation requires Portal JS which we have proved can be done
- There is no dedicated template builder BUT CKAN has a lot of API and integration potential

--- 

## Specific User Needs
This specific user need has been isolated as it's own study as it is at the intersection of tech capability/user needs and functional requirements.
Users need to build and maintain custom templates that describe a range of metadata objects across an array of themes and topics and therefore an array of vartiable decriptors too.
Deeper research was conducted to better understand what is possible across NADA and CKAN with regards to template creation and curation.

Research:
<details open>
  <summary>NADA Metadata Template Creation and Editing</summary>  
I asked Claude if NADA had reasonable metadata template creation and editing capability.

Research response from Claude:

This is the NADA catalog documentation (IHSN's data cataloging platform), and short answer: not really — metadata template editing isn't presented as an "easy" built-in feature.

Here's what the page actually says:
Metadata generation has three routes, and the built-in one is the weakest:
  - Metadata can be generated using specialized metadata editors, using programming languages like R or Python, or directly in NADA using the administrator interface (for all data types except geospatial). github
  - For microdata and geographic datasets, it's highly recommended to use a specialized metadata editor due to the complexity of the metadata standard. github
  - Most tellingly: the NADA administrator interface provides a user-friendly option to generate metadata, but should not be the preferred option, as it does not provide the advanced functionalities of specialized metadata editors — especially for microdata — nor the flexibility and reproducibility that the API option provides. github

So this overview page effectively steers admins away from relying on NADA's own UI for metadata work, especially for microdata, in favor of either dedicated external metadata editors or scripting against the API (via NADAR/PyNADA).
This particular page doesn't go into UI mechanics for editing templates specifically — that detail would likely live in the "Content by data type" or "Site administration" sections it links to. Want me to check one of those (e.g., the microdata content page or the admin web UI section) for more specifics on the actual editing experience?When prompted to dig deeper Claude produced this response:

Confirmed: this is not an easy metadata-template editing tool. In fact the microdata page is more explicit and more negative than the overview page suggested.

What the web interface can actually do for metadata:
1. Upload pre-existing metadata (the recommended path) — you bring a DDI-compliant XML file plus an RDF file, generated externally by a dedicated editor like Nesstar Publisher or the World Bank's Metadata Editor, and NADA just ingests them. This isn't "editing a template" in NADA at all — the real editing happens elsewhere.
2. Build metadata "from scratch" directly in NADA's own interface — this exists, but the documentation is unusually blunt about its limits: this option is limited to the study description section of the DDI metadata standard, and the file and variable description sections are not included in the metadata editor embedded in the NADA web interface. Since the DDI should contain a description of the variables included in the data files, preferably with summary statistics, and generating variable-level metadata can be a very tedious process as some datasets may include hundreds or thousands of variables, NADA's built-in editor simply can't produce complete, rich metadata for anything but the simplest datasets. githubgithub
3. The documentation's own guidance is to avoid the built-in editor: the use of this option is not recommended except for cases when no file and variable description is available; in other cases, the use of a specialized metadata editor or the more complex programmatic option are recommended. github

The admin web UI section reinforces this — it's organized around site operations (studies, users, collections, site config, etc.), and for microdata specifically it points you to the "Add study" → DDI/RDF upload workflow, with the limited from-scratch editor as a fallback only.

Bottom line: NADA is fundamentally a cataloging and publishing tool, not a metadata-editing tool. Its own docs steer administrators toward external specialized editors (Nesstar Publisher, World Bank Metadata Editor) or scripting via R/Python + API for anything beyond trivial datasets, and explicitly flag the built-in web editor as incomplete and not the preferred route — especially for microdata.
</details>

<details open>
  <summary>CKAN Metadata Template Creation and Editing</summary>
I also asked Claude if CKAN had reasonable metadata template creation and editing capability.

Research response from Claude:

This is a different documentation structure than NADA — no dedicated "user guide" walkthrough of metadata entry from the overview. The relevant pages appear to be under Extending guide → "Customizing dataset and resource metadata fields using IDatasetForm" and Maintainer's guide → "Form Integration". Let me check both.

This is a clear answer, and it's a third distinct pattern compared to NADA and the Metadata Editor: No, CKAN's official documentation does not describe an easy way to create or edit metadata templates. Modifying CKAN's metadata schema is a developer task, not an admin/curator task.

Here's what the docs actually show:
There's no visual template manager, no admin UI for this at all. The only path documented for customizing dataset/resource metadata fields is via IDatasetForm, a plugin interface that requires:
Writing a Python plugin (a ckanext-* package) with a class that implements IDatasetForm and inherits from SingletonPlugin and DefaultDatasetForm.
Manually overriding three separate schema methods — create_package_schema(), update_package_schema(), and show_package_schema() — each returning a dict of validator/converter functions per field.
Writing custom Python validators by hand (with three different function signatures depending on what you need) if you want anything beyond CKAN's built-ins.
Overriding Jinja2 HTML templates (package_metadata_fields.html, package_basic_fields.html, additional_info.html, resource_form.html, etc.) just to get a new field to render in the web form and on the dataset page — this is manual front-end templating, not a form-builder.
Separately wiring up tag vocabularies via API calls (vocabulary_create, tag_create) if you want a constrained dropdown-style field, plus template helper functions to surface them.
Even something as small as changing the sort options on the search page requires overriding another template.

The docs themselves acknowledge the manual complexity by pointing to a third-party extension, ckanext-scheming, as an alternative — this lets you define a metadata schema in a YAML or JSON file instead of raw Python, with custom validation and snippets. But this isn't core CKAN; it's an unofficial community extension you'd need to separately install, and the core docs don't walk through it.

Bottom line — comparing all three tools:
ToolMetadata template editingNADABuilt-in UI editor exists but is explicitly discouraged by its own docs, especially for microdata; recommends external tools instead World Bank Metadata EditorPurpose-built Template Manager with a visual navigation tree, duplicate/export/import/preview, role-gated — genuinely easy, first-class feature CKAN No admin UI at all for this; requires writing a Python plugin, overriding schema functions, hand-coding validators, and manually editing HTML templates — this is developer/sysadmin work, not something a data curator does.

So CKAN sits at the opposite end from the Metadata Editor: powerful and flexible if you're a developer, but nowhere close to "easy" for a non-technical user trying to create or adjust a metadata template.
</details>

<details open>
  <summary>NADA and WorldBank Metadata Editor</summary>
I then asked Claude if the WorldBank Metadata Editor could be considered a suitable way to build and edit metadata upstream from NADA.

Research response from Claude:

Yes — this is a fundamentally different situation than NADA. The World Bank Metadata Editor is genuinely built for template editing, not just data entry.

It has a dedicated, GUI-based Template Manager, purpose-built for exactly this:
Templates are described as tailored subsets of a metadata standard's elements, letting an organization customize labels, required/recommended status, descriptions/instructions, controlled vocabularies, default values, validation rules, and even add fields not in the original standard at all.
You get a visual navigation tree showing the template's structure, with a toolbar to add/remove/reorder elements, create groups and sub-groups, and drag elements between them.
The normal workflow is genuinely easy: start from a non-editable core template (one version has all standard elements, others are curated "most important fields" starter sets), then DUPLICATE it and edit the copy — no need to build from zero.
Rich supporting actions exist right in the UI: EXPORT/IMPORT (as JSON, for sharing templates across organizations), PREVIEW (renders as HTML), TABLE (exports to something pasteable into Excel), PDF (generates an instruction guide for curators), REVISIONS (change history), and SHARE (granular view/edit permissions per template).
Field-level editing is detailed but still form-based — you set key, label, type, status, description, display style (text/textarea/date/dropdown), controlled vocabulary source, defaults, and validation rules all through UI panels, not by hand-editing schema files.
Access is role-gated (a Template manager role, or per-template SHARE access) rather than open to everyone — sensible for governance, but it does mean not just any user can edit templates.

Bottom line: where NADA's own docs actively discourage using its built-in editor for anything beyond trivial metadata, the Metadata Editor's docs describe template editing as a first-class, designed-for-purpose workflow with a real UI, safeguards (validation, schema alignment checks), and convenience features (duplicate-from-core, export/import, preview). 

This tool is the one referenced earlier as the "specialized metadata editor" NADA recommends using upstream — and template creation/editing is clearly central to its design, not an afterthought.
</details>

<details open>
  <summary>CKAN and WorldBank Metadata Editor</summary>
I finally asked Claude if it was possible to feed-in or integrate CKAN & WorldBank Metadata Editor.

Research response from Claude:

Based on the Metadata Editor docs (both the "Publish to NADA" page and the wider "Publishing data and metadata" section), the answer is: not directly, out of the box — CKAN is not a supported publish target.

Here's the picture:
Built-in publishing is NADA-only. The docs' "Publishing data and metadata" section contains exactly one page: "Publish to NADA." Indicator projects, for example, can publish study metadata, external resources, and (when set up) data structure and observation data directly to a configured NADA catalog. There is no equivalent "Publish to CKAN" page or button anywhere in the documentation.

This is confirmed by the tool's own developers, not just an absence in the docs. A conference abstract from the World Bank team describing the Metadata Editor states plainly: the editor offers built-in support for publishing directly to NADA data catalogs, and for other DDI-compliant catalogs, the API can be utilized for seamless automation. In other words, NADA gets a dedicated one-click integration; everything else — CKAN included — is left to custom API work.

What could bridge the gap (not documented, but technically plausible):
The Metadata Editor has a full REST API and can export metadata in several formats — JSON, XML/RDF, SDMX, PDF — per project type.
CKAN, on its side, has an API and can ingest datasets via harvesters (e.g., the community ckanext-dcat extension, which can harvest RDF/DCAT feeds) or via direct API calls to package_create.
So a determined technical team could write a script or small integration that pulls metadata out of the Metadata Editor (via its API/export) and pushes it into CKAN (via CKAN's API), mapping DDI/Dublin Core/ISO 19139 fields onto CKAN's schema (including any custom IDatasetForm fields you built, per the earlier CKAN discussion).
But this is not a documented, supported workflow — it would be bespoke integration work, not a feature either tool ships with.

Bottom line: The Metadata Editor is built to feed NADA specifically. Getting metadata into CKAN would mean building your own API bridge — exporting from one system's API and importing via the other's — rather than using anything the documentation describes as ready-made.
</details>

## Summary
The following recommendations are bing made after reviewing both tools in relation to their appropriateness for the NT-SDF project and CivicView.

NADA is an attractive modern catalog system that has add on functionality that allows users to build templates.
HOWEVER it is maintained by one person. This is a high risk consideration and is partly evident in the tool itself: Some help features did not work, some system nav functions were broken and directed to the incorrect places etc.

CKAN, while the native UI is seemingly "old fashioned" the system is a solid, trusted DMS in the space. As it stands, it does not have a flexible user interface editor HOWEVER it is highly flexible in terms of its API connectivity and ability to serve as a database instead of an interface. This gives us a massive range of options in temrs of how metadata and resources are served to our users.
It is also able to connect to WorldBank Metadata Editor via a custom API allowing us to potentially tap into the good conventions utilised there.

Our recommendation for this implementation is to use CKAN as a back end system and build a front end UI that truly matches our user requirements.
