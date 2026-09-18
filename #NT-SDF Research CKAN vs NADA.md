#NT-SDF Research CKAN vs NADA

##Task
Run a review comparing [NADA](https://microdata.worldbank.org/home) to [CKAN](https://datasets.edge.durban/dataset/)

###Purpose
To determine which platform is more suited for the NT-SDF metadata catalog project from a user experience perspective.
A truly intuitive and engaging system for the browsability of data, datasets, metadata and associated assets is a difficult nut to crack as evidenced by the range of data management and cataloging tools out there. 
Over the years we have come across a large range of systems, all of which have a very similar look and feel. One could assume that his has become standard because users like this way of browsing but our research and engagement over the last 8 years tells us that this may be more a case of emulating the "thing" that came before than responding to user needs. 
This presents an opportunity to disrupt how government workers, researchers and the public (and the full range of possible stakeholders) find, engage and interact with data and metadata.

###Considerations
Our proposed system has to address a number of user requirements which will affect our final choice of platform.
- Is it intuitive and easy to use?
- Is it easy to maintain?
- Is it easy to integrate with other systems?
- Is it easy to customize?
- Can the user create custon metadata objects? (specific project requirement)
- Can it be made engaging for portal visitors?

###Requirements
- A review of the two platforms
- A comparison of the two platforms using a custom rubric
- A recommendation for the best platform for the NT-SDF metadata catalog project

###Methodology
1. Select case study examples to examine:
  - Our CKAN exemplar: [EDGE Data Portal](https://datasets.edge.durban/dataset/) was used to test CKAN
  - Our NADA exemplar: [World Bank Metadata Libary](https://microdata.worldbank.org/home), [DataFirst](https://www.datafirst.uct.ac.za/dataportal/index.php/catalog) and [Demo NADA Catalog](https://nada-demo.ihsn.org) were used to test NADA
2. Understand user flows - how easy/difficult is it to get straight to useable data/resources?
  - Screengrabs were taken of the portals in question and the flows plus features were noted in [this Figjam document](https://www.figma.com/board/CpYG38S9cG5lOuRSOIxU7w/NT---Metadata-Portal--User-Journeys---Wireframes-?node-id=76-554&t=6M2DscstwEdsHJNR-1)
3. What features and functionality exist on both OR are unique to one system that are relevant to this work?
  - This review was done as part of the user flow exercise described above
4. Compare systems from a user experience perspective using [this custom scoring rubric template for data portals](https://docs.google.com/spreadsheets/d/1bmh3BqSX8lLmW6CLQIUdYufXuO7OFCKEIuiS87EanZQ/edit?usp=drive_link) created by OCL + Claude

###Resources
- [NADA](https://microdata.worldbank.org/home)
- [CKAN](https://datasets.edge.durban/dataset/)
- Designs
_ User Flows

---

##Results

###Caveat
*It is important to note that the results above are based on what currently exists and doesn't take into consideration what is possible but not yet implemented.*
*These results contain some recommendations which, if adopted, will likely require custom build time.*

###User Flows
Looking at the [user flows](https://www.figma.com/board/CpYG38S9cG5lOuRSOIxU7w/NT---Metadata-Portal--User-Journeys---Wireframes-?node-id=76-554&t=6M2DscstwEdsHJNR-1) we were able to understand how a user might arrive at a landing page and then navigate into a metadata object or dataset. 
We were also able to appraise what that experience would be like if a user was directed straight to resource/download dataset.
We found the following:

**[DataFirst](https://www.datafirst.uct.ac.za/dataportal/index.php/catalog)** has a landing page which can send the user either directly to the catalog or can send them on a gradutaed journey through an explainer first.
Review
  - This was the longest journey and while it did offer a direct route to data, that route was slightly obscured and the longer journey seems to be prioritised via attractive story-type cards with imagery 
  - The longer journey goes some way to making the subject matter more understandable to a wider audience but it requires numerous clicks to get to the downloadable and once you are at the final point, you are very much in a typical data catalog space
  - The portal is attractive with imagery and blog entries but it is clear that this requires a fair amount of curation which the NT-SDF team have explicitly stated they do not have capacity to handle

Takeaways
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

**[World Bank Metadata Libary](https://microdata.worldbank.org/home)** and **[Demo NADA Catalog](https://nada-demo.ihsn.org)**
