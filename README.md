# biosketch
Scripts for managing NSF biosketches in the SciENcv format.

## Why?

As of May 2020, NSF (and DOE) have moved to the NIH-style [SciENcv format](https://www.ncbi.nlm.nih.gov/sciencv/) for proposal biosketches. As of June/July 2021, importing references into SciENcv can be painful if your references are not already in PubMed, which excludes prominent astronomy and astrophysics journals such as the Astrophysical Journal, A&A, MNRAS, etc. and a number of physics journals from Elsevier. This project provides some ways to reduce the pain by showing you how to manually import reference in RIS format.

## How?

Until SciENcv automatically connects to publication databases like Scopus, your best bet as an astronomer or physicist is to grab your publication list from [inspire-hep](https://inspirehep.net) or [NASA ADS](https://ui.adsabs.harvard.edu/) and massage them into the proper format. Here are instructions for both options.

### Using inspire-hep

The inspire-hep bibliography exporter does not support RIS format, so follow these steps:
1. Export your citations in BibTeX format.
2. Use the [bibutils](https://ctan.org/pkg/bibutils) library to convert your citations to XML: `bib2xml INSPIRE-CiteAll.bib > INSPIRE-CiteAll.xml`.
3. Use the [bibutils](https://ctan.org/pkg/bibutils) library to convert the XML to RIS format: `xml2ris INSPIRE-CiteAll.xml > INSPIRE-CiteAll.ris`.
4. Upload the citations in the SciENcv portal using the RIS file you created.

### Using NASA-ADS

The NASA ADS author search will export your publications in RIS format but it includes full author lists, full abstracts, and lots of other metadata that can easily make the RIS file >10MB. The SciENcv bibliography upload will not be able to handle RIS files this large. In this case, use the python script attached in this project to significantly reduce the information per entry to a manageable size:

`python reduce_ads_ris.py export-ris.txt -o NASA-ADS_citations.ris`,

where `export-ris.txt` is the initial download from NASA ADS. I recommend that when you download the citation list from ADS, you enable the **refereed** checkbox in the selection menu so that you don't include unpublished or unrefereed proceedings in your CV.
