Scraping: https://www.census.gov/hfp/btos/about
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.census.gov/hfp/btos/about
  Settled (dom-quiet, 2185ms)
  Extracting content...
  Extracted 9888 characters

--- Content ---

### Purpose

The Business Trends and Outlook Survey (BTOS) is a continuous fielded survey that provides high-frequency, nationally representative data on U.S. employer businesses every 2 weeks. The survey provides local, state, and federal officials near real-time data for policy and decision-making, including after natural disasters or during economic crises. The BTOS also provides insights into recovery after these events.

The BTOS sample consists of approximately 1.2 million businesses split into 6 panels (approximately 200,000 cases per panel). Businesses in each panel are asked to report once every 12 weeks for about a year (4-5 times within a year). Data collection occurs every 2 weeks. The BTOS is comprised of a set of core questions and supplemental content, which is included as needed.

The BTOS collects information on a wide range of business conditions. Among other topics, sampled companies are asked about their current performance, changes in revenue, employment, hours worked, location operating status, demand, and prices. For most concepts, businesses are asked about the previous 2 weeks and for a 6-month projection.

### Coverage

The target population for BTOS is all nonfarm, employer businesses that are in the United States, District of Columbia, and Puerto Rico. The following industries are designated as out of scope for the BTOS:

- Agriculture production (NAICS in \[“110000,” “111,” “112”\])
- Railroads (NAICS = "482")
- U.S. Postal Service (NAICS = "491")
- Monetary Authorities – Central Bank (NAICS = "521")
- Funds, Trusts, and other financial vehicles (NAICS = "525")
- Religious grant operations and religious organizations (NAICS = "813")
- Private households (NAICS = "814")
- Public administration (NAICS = "92")
- Unclassified with legal form of organization as tax-exempt or unknown

Businesses classified without a 2-digit NAICS (NAICS = "00") are not included.

For the first year, the BTOS data are representative of all single-location employer businesses in the U.S. economy, excluding farms (July 18, 2022 – September 10, 2023). The last publication to include only single-location employer businesses was September 14, 2023. For the second year and subsequent years, the BTOS data includes all employer businesses (single-location and multi-location) in the U.S. economy, excluding farms (September 11, 2023 – present).

### Content

#### Core Content

The BTOS is a voluntary, qualitative survey. Questions are designed with the intention of collecting information on a wide range of business conditions via categorical responses (mostly increased, decreased and no change) while minimizing respondent burden. Sampled companies are asked about their current performance, changes in revenue, employment, hours worked, location operating status, demand, and prices, among other topics. For most concepts, businesses are asked about the previous 2 weeks and for a 6-month projection. At times, core content has also included emerging areas of interest, such as business use of artificial intelligence and work from home.

#### Super Intelligence or SI (formerly referred to as Artificial Intelligence or AI) Core Content

On October 26, 2023, BTOS started publishing two core questions to measure the use of Super Intelligence or SI (collected as Artificial Intelligence or AI). Respondents were asked about SI use within the past 2 weeks and plans to use SI within the next 6 months. Starting with the November 17, 2025 collection, based on expert feedback and cognitive testing, [BTOS updated](<./downloads/AI Question Wording Updates.pdf>) these two core questions with broader language to help respondents capture their business use of SI. Specifically, business use of SI in “producing goods or services” was replaced by “any of its business functions.” Beginning with the October 19, 2026 collection, [instrument wording](<./downloads/BTOS Content V5 Core Round 3, 4.pdf>) was updated due to [Executive Order 14434](https://www.whitehouse.gov/presidential-actions/2026/09/inaugurating-the-era-of-super-intelligence/).

#### Supplemental Content

BTOS supplements are designed to build on the core survey content. Past supplements have expanded on existing core questions, such as SI adoption and work from home (WFH). While the core questions are intended to track ongoing economic trends, supplemental questions are designed to provide a one-time snapshot with additional detail on a specific, timely topic. For tabulating supplements, non-response adjustment is performed for each biweekly panel, but all responses are pooled together, and the weights are adjusted to reflect that the entire sample is included in estimation. We pool together the 6 panels (12 weeks) and tabulate that data. We carefully manage respondent burden when considering supplemental content. Supplements thus far have been capped at ten minutes.

The [first supplemental content](<./downloads/BTOS Content V2 Supplement 11.29.2023_Watermarked.pdf>) was added to BTOS from December 2023 to February 2024 to provide more detailed information about businesses’ use of SI (collected as AI). There are 13 questions in the supplement in addition to the two core SI questions. The two core SI questions remain on the survey.

The [second supplemental content](./downloads/BTOSContentV311.20.24Cycle2WFHSupplement.pdf) was added to BTOS from November 2024 to January 2025. Existing measures of WFH reveal significant data gaps in understanding its scope, particularly from the business perspective. To address this, eleven WFH questions were developed for the BTOS, covering the share and frequency of WFH, challenges, management policies, and business impact.

The [third supplemental content](<./downloads/BTOS Core and AI Content.pdf>) was added to BTOS from November 2025 to February 2026 to provide more detailed information about businesses’ use of SI (collected as AI). The questions were intended to capture SI use within the firm, by worker tasks, and by business functions. The primary intention of this supplement was to understand the difference in SI adoption from the worker perspective versus the firm perspective.

The [fourth supplemental content](<./downloads/BTOS Content V5 Core and SI Instrument - Cycle 2-Tagged.pdf>) will be added to BTOS from October 2026 to January 2027 and is designed to again provide more detailed information about businesses’ use of SI (collected as SI). Many of the same questions from the third supplement were again used, along with additional new questions regarding the impact of SI on the workforce and hiring.

Please refer to the [Downloads and Documentation](/hfp/btos/data_downloads) tab for the full BTOS questionnaires.

### Frequency

The BTOS has a biweekly data collection schedule. Estimates are published every other Thursday. Edits and benchmarking are not performed, although data are reviewed for accuracy prior to release. Note - Supplemental data are published as pooled estimates over 6 data collection periods.

### Methods

Please refer to the [Methodology](/hfp/btos/methodology) tab for information about the frame, sample, data collection and data tabulation.

### Products

Every two weeks, on Thursdays at 10am, BTOS releases multiple data products tabulated at the national level, by state, two- and three-digit NAICS sector, employment size class, the top 25 most populous MSAs and sector-by-employment-size tables. The BTOS does not do revisions.

The BTOS is a firm-level survey, so multi-unit businesses operating across states or sectors are labeled as “XX” in published outputs.

Some questions are also tabulated as indexes to provide key performance indicators for certain topics. The BTOS data are available through static visualizations, Excel tables, and an API.

### Indexes

Each index is a weighted average of the percentage estimates for that question. The indexes measure the breadth of change for the variable of interest. They capture the extensive margin of change, in that an index moving toward 100 reflects the extent to which the situation for that variable is increasing and movement towards 0 reflects the extent to which the situation for that variable is decreasing while a value near 50 suggests a preponderance of businesses reporting no change. Depending on the question, increasing could have a negative connotation, such as the question on prices. Refer to [Index Methodology](./downloads/research/index_measure_v1.pdf) for more information on the construction of BTOS indexes.

### Limitations

BTOS estimates are subject to error from a variety of sources, including sampling error and nonsampling error, such as coverage error, measurement error, and processing error. For a more detailed discussion of error sources, please see the [Methodology](/hfp/btos/methodology) tab. BTOS estimates may be subject to nonresponse bias if businesses that respond to the survey are systematically different from businesses that do not. An BTOS nonresponse biases analysis is forthcoming.

### Disclosure Statement

Disclosure is the release of data that reveals information or permits deduction of information about a particular survey unit through the release of either tables or microdata. Disclosure avoidance is the process used to safeguard each survey unit’s identity and data from disclosure. Although it may appear that a table shows information about a specific survey unit, the Census Bureau has taken steps to protect a unit’s data that may be “at risk” of disclosure while making sure the results are still useful.

The Census Bureau has reviewed this data product to ensure appropriate access, use, and disclosure avoidance protection of the confidential source data (Project No. P-7529868, Disclosure Review Board (DRB) approval number: CBDRB-FY26-0278).

### Contact Us

Contact us at [econ.btos@census.gov](mailto:econ.btos@census.gov)
