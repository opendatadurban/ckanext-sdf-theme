# NT-SDF Reserach CKAN vs NADA

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

### Resources
- [NADA](https://microdata.worldbank.org/home)
- [CKAN](https://datasets.edge.durban/dataset/)
- Designs
_ User Flows

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

---

[CKAN - EDGE Data Portal](https://datasets.edge.durban/dataset/)
Gets users to the usable data/resources relatively quickly.
Review:
- We had previously worked in the CKAN page builder space (used to build landing pages and about pages etc) before and found it limiting. CKAN does however have powerful Portal JS compatability that offers broad flexibility when it comes to the UI and UX of the pages around the data portal
- ss

--- 

##Specific User Needs
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
