Scraping: https://nvd.nist.gov/general/news
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://nvd.nist.gov/general/news
  Settled (dom-quiet, 1865ms)
  Extracting content...
  Extracted 26294 characters

--- Content ---

NIST maintains the National Vulnerability Database (NVD), a repository of information on software and hardware flaws that can compromise computer security. This is a key piece of the nation’s cybersecurity infrastructure.

## news updates

### August 26, 2026: Technical Update: NVD SSVC and “affected” Data Delivery

**Outlined Changes:**

The NVD is updating the CVE Detail page to now include the “affected” list (the list of vulnerable product configurations) and the “SSVC” (Stakeholder-Specific Vulnerability Categorization) score. When available, both sets of data will now be shown on the CVE detail page, with the ‘affected’ section above the ‘Change History’ and SSVC data shown within the ‘Metrics’ section.

The NVD is replacing the full “affected” JSON payload that has been embedded in each Audit History entry with a lightweight reference directly to the CVE within the GitHub repository. Each audit record will now contain a URL that points to the CVE. This covers additions, modifications, or removals made to the “affected” product list. This shift reduces data transfer required for frequently changing and large affected data entries.

The NVD’s new model keeps the current CVE detail endpoint (/cves/) unchanged; it still returns the latest full “affected” JSON for a given CVE (the /cvehistory feed changes). Previously, every entry carried the complete affected JSON under an affected key.

Starting August 26th, 2026, the entries will not include the affected data but will contain a GitHub Link (a direct URL to the CVE record on GitHub).

**Why are there Changes?**

Offloading the large and frequently changing “affected” lists to GitHub links significantly reduces bandwidth and payload sizes in the /cvehistory feed, allowing downstream tools to consume incremental audit updates much more efficiently.

### June 17, 2026: NVD Deployment Update: SSVC and CVE Affected Data Now Available Across NVD Data Feeds and APIs

On June 17, 2026, the National Vulnerability Database (NVD) deployed an expansion to its vulnerability assessment metrics and data schema. This update expanded information available for a CVE record to now include Stakeholder-Specific Vulnerability Categorization (SSVC) data sourced from the CISA-Authorized Data Publisher (CISA-ADP), supplementing existing Common Vulnerability Scoring System (CVSS) scores. Furthermore, the NVD will also include "affected" information as defined in the CVE Record Format.

More Information

**New SSVC and Affected Data Schemas**

The NVD has updated its API to include two new structured data schemas for enhanced vulnerability intelligence:

**SSVC v2.0.3**

The NVD now provides a Computed SSVC Score that shows how a vulnerability priority was decided.

- **Schema Resource:** [https://csrc.nist.gov/schema/nvd/api/2.0/ssvc-v2.0.3.json](https://csrc.nist.gov/schema/nvd/api/2.0/ssvc-v2.0.3.json)

**CVE Affected v1.0**

The NVD now includes the list of “affected” software as indicated on a CVE record.

- **Schema Resource:** [https://csrc.nist.gov/schema/nvd/api/2.0/cve\_affected\_1.0.json](https://csrc.nist.gov/schema/nvd/api/2.0/cve_affected_1.0.json)

**Operational Impact & Deployment Advisory**

**Data Refresh and Synchronization:** The deployment process affected approximately 95% of all existing vulnerabilities within the NVD. Consequently, every updated record now includes a new change log entry and an updated “lastModified” timestamp.

**Warning on File Size:** Due to the large scale of these updates, the CVE-Modified feed will experience an increase in file size for a duration of eight days following the deployment. Organizations utilizing automated synchronization scripts or ETL pipelines must ensure that their environments are configured to handle significantly larger payloads to avoid timeout errors or memory overflows.

**API Performance:** Users querying the API should expect larger JSON payloads for individual CVE records. While the schema expansion is additive, increased latency may be observed during the initial period of high-volume data refreshes.

**System Stability:** There have been no changes to the vulnerability status levels associated with this update. Although the NVD vulnerability schema has been expanded to support the new data elements, the changes were designed to maintain compatibility with existing consumer workflows and processing pipelines.

**Developer Resources**

Developers integrating with the NVD APIs are encouraged to review the updated NVD Vulnerabilities API and schema documentation on the [NVD Developer Vulnerabilities Page.](https://nvd.nist.gov/developers/vulnerabilities)

The CVE API response documentation includes:

- Schema definitions for the newly available affected data.
- Schema definitions for SSVC assessment information.
- Detailed field-level descriptions for CVE API response objects

### May 28, 2026: NVD Will Now Include SSVC and Affected Data Within the CVE Feed and CVE API Results

Starting on June 17, 2026, the NVD will expand to include two distinct types of **vulnerability assessment metrics**. While the database has always provided Common Vulnerability Scoring System (CVSS) scores, we are now expanding to also provide Stakeholder-Specific Vulnerability Categorization (SSVC) data from the Cybersecurity and Infrastructure Security Agency-Authorized Data Publisher (CISA-ADP). This update will allow organizations that need this information to access it via the NVD.

More Information

In addition, the NVD had already included information related to the [Known Exploitable Vulnerabilities (KEV) catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) data and other available enrichment information present within this part of the CVE record. With the change announced here, the NVD will also include any provided “affected” information as represented in the [CVE Record Format](https://github.com/CVEProject/cve-schema/releases/tag/v5.2.0). Both additional pieces of information will be available in the data feed and API. Future updates to the website will enable viewing this information on the vulnerability detail page for a particular record.

**How We Will Implement this Update**

On June 16, 2026 between 8:00 PM EDT and 12:00 AM EDT, we will run a process to update the NVD to now include SSVC and “affected” information. This process will take several hours and will complete sometime on June 17, 2026. Every updated record will include a new change log entry and will have an updated ‘Last Modified’ date. No status change will occur because of the update. The update process will affect about 95% of all vulnerabilities currently in the NVD. These changes will be visible to end-users between 8:00 AM EDT and 2:00 PM EDT on June 17, 2026.

**What You Need to Do**

The “ [CVE-Modified” feed](https://nvd.nist.gov/vuln/data-feeds) will be much greater in size than normal for the eight-day period following the update process. If you have processes that use this file, prepare to receive a larger file for this period of time. If you use the API, you should also expect larger results for CVE records during this time period. While the vuln schema is changing to reflect these additions, existing processes will not be impacted by this change.

### April 28, 2026: NVD to Update Inaccurate CVSS v4 Records

On April 15th, we were alerted to the presence of inaccurate numerical CVSS v4.0 scores for certain CVE records. After analyzing this issue, we determined that, due to an error in how the numerical portion of the CVSS v4.0 scores are calculated and stored, approximately 4,500 CVE records currently have an incorrect numerical score.

Click "More information" below to learn more about the problem, what we are doing to fix it, and actions that users should take to ensure their vulnerability data are up to date.

More information

#### Scope of the issue

Only the calculated numerical CVSS v4.0 scores were affected. Approximately 4,500 CVE records (19% of CVE records that have a v4.0 score) were assigned a CVSS numerical score higher than the correctly calculated value. Fewer than 30 CVE records were assigned a score lower than the correctly calculated value.

#### How we are resolving this issue

We will run a script to update all affected CVE records on April 28, 2026, at 9:00 pm EDT. To ensure transparency and traceability, all updates will be documented with audit entries. In addition, the 'modified date' of all affected CVE records will be updated to ensure these changes are captured by the Vuln API lastModStartDate and lastModEndDate parameters.

#### Actions required for users

After we have implemented this fix, API users that use the lastModStartDate and lastModEndDate parameters will automatically ingest the corrected scores next time they sync their data. API users that do not use the lastModStartDate and lastModEndDate will need to to ensure these updates are downloaded appropriately.

#### What we are doing to prevent a recurrence

The underlying error which caused us to use incorrectly calculated v4.0 CVSS numerical scores has been corrected. To ensure that a similar error does not go undetected, we have implemented a robust, automated score verification process that will be deployed by the end of May.

### April 15, 2026: NIST Updates NVD Operations to Address Record CVE Growth

**New risk-based model will allow NIST to manage current CVE volume while modernizing the NVD for long-term sustainability.**

NIST is changing the way it handles cybersecurity vulnerabilities and exposures, or CVEs, listed in its [National Vulnerability Database (NVD)](https://nvd.nist.gov/). In the past, NIST’s NVD program aimed to analyze all CVEs to add details — such as severity scores and product lists — that help cybersecurity professionals prioritize and mitigate vulnerabilities. Going forward, NIST will add details, or “enrich,” those CVEs that meet certain criteria, which are explained below. CVEs that do not meet those criteria will still be listed in the NVD but deemed as "lowest priority" and will not be immediately enriched by NIST.

More information

This change is driven by a surge in CVE submissions, which increased 263% between 2020 and 2025. We don’t expect this trend to let up anytime soon. Submissions during the first three months of 2026 are nearly one-third higher than the same period last year.

We are working faster than ever. We enriched nearly 42,000 CVEs in 2025 — 45% more than any prior year. But this increased productivity is not enough to keep up with growing submissions. Therefore, we are instituting a new approach. The changes described below will allow us to focus on the most critical CVEs while being transparent about how we are managing our current workload. They will also allow us to stabilize the program while we develop the automated systems and workflow enhancements required for long-term sustainability.

##### New Prioritization Criteria

Starting on April 15, 2026, we will prioritize the following CVEs for enrichment:

- CVEs appearing in [CISA’s Known Exploited Vulnerabilities (KEV) Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
	- Our goal is to enrich these within one business day of receipt
- CVEs for software used within the federal government
- CVEs for [critical software](/document/definition-critical-software-under-executive-order-eo-14028 "Definition of Critical Software Under Executive Order (EO) 14028") as defined by Executive Order 14028

All submitted CVEs will still be added to the NVD. However, those that do not meet the criteria above will be categorized as “Lowest Priority - not scheduled for immediate enrichment.” This will allow us to focus on CVEs with the greatest potential for widespread impact. While CVEs that do not meet these criteria may have a significant impact on affected systems, they generally do not present the same level of systemic risk as those in the prioritized categories.

These criteria may not catch every potentially high-impact CVE. Therefore, users can request enrichment of any lowest priority CVEs by emailing us at [nvd@nist.gov](mailto:nvd@nist.gov). We will review those requests and schedule the CVEs for enrichment as resources allow.

A full definition of critical software and a description of our new workflow, including how we will order our processing queue, is available on the [NVD website](https://nvd.nist.gov/general/cve-process).

##### Streamlining Severity Scores

Until now, NIST has provided its own severity score for all submitted CVEs, even if the CVE Numbering Authority that submitted it had already provided a severity score. Going forward, we will no longer routinely provide a separate severity score for those CVEs. This will reduce duplication of effort and allow us to focus our resources more effectively. Users can request that we provide a separate severity score for specific CVEs by emailing us at the address above.

##### Handling of Modified CVEs

We are changing our process for reanalyzing enriched CVEs that have been modified subsequent to enrichment. While our previous policy was to re-analyze all modified CVEs, we will now do so only if we are aware of a modification that materially impacts the enrichment data. Users can request that we reanalyze specific modified CVEs by emailing us at the address above. Because of this process change, all CVEs marked as deferred last year (see [April 2, 2025: NVD General Announcement](https://www.nist.gov/itl/nvd#april0225)) will be moved to “Modified After Enrichment.” Due to the large number of CVEs involved, we will be recategorizing these CVEs in batches over the next two weeks.

##### The CVE Backlog

Starting in early 2024, the NVD developed a significant backlog of unenriched CVEs. Unfortunately, we have been unable to clear that backlog, in part due to the increasing rate of submissions. Therefore, when we implement the new prioritization criteria described above, we will move all backlogged CVEs with an NVD publish date earlier than March 1, 2026, into the “Not Scheduled” category. We will consider enriching those earlier vulnerabilities, applying the new prioritization criteria above, as resources allow. (Note that the backlog does not include any CVEs in the KEV Catalog, as we have always prioritized those for enrichment, in keeping with our long-standing risk management approach.)

New Status Labels and Other Information

To better communicate CVE status, we are updating CVE status labels and descriptions. More details are available on the [CVE statuses page](https://nvd.nist.gov/vuln/vulnerability-status). Additional details on our new process are available on our [CVEs and the NVD Process page](https://nvd.nist.gov/general/cve-process). Finally, we have updated the [NVD Dashboard](https://nvd.nist.gov/general/nvd-dashboard) to accurately report the status of all CVEs and other NVD statistics in real time.

We recognize that these changes will affect our users. However, this risk-based approach is necessary to manage the current surge in CVE submissions while we work to align our efforts with the needs of the NVD community. This shift also allows us to dedicate the resources required to develop the automated systems and workflow enhancements that will ensure the program’s long-term sustainability. We look forward to announcing those improvements as we make them.

NIST is committed to maintaining the NVD as a critical component of the nation’s cybersecurity infrastructure. By evolving the NVD to meet today’s challenges, we can ensure that the database remains a reliable, sustainable and publicly available source of information about cybersecurity vulnerabilities. We appreciate the continued collaboration of our partnering agencies and the user community as we make these necessary adjustments.

This update is also [available here](/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth "NIST Updates NVD Operations to Address Record CVE Growth").

### Sep 16, 2025: NVD Technical Update

We plan to deploy updates to NVD systems on September 16th, 2025. This deployment includes the following relevant changes:

- **Updates to the process for API Key provisioning:** API keys are now issued following user interaction with a form on the page, rather than being displayed immediately upon confirmation page load. Information for requesting an API Key can be found here: [https://nvd.nist.gov/developers/request-an-api-key](https://nvd.nist.gov/developers/request-an-api-key)

### Aug 20, 2025: NVD Technical Update

We plan to deploy updates to NVD systems on August 20th 2025. This deployment includes the following relevant changes:

- **Decommissioning of Legacy Data Feed Files:** As of **August 20th, 2025**, the following legacy Data Feed files have been removed from the NVD [Data Feeds Page](https://nvd.nist.gov/vuln/data-feeds) and are no longer available for access or download
	- 1.1 Vulnerability Feeds
		- 1.0 CPE Match Feed
		- XML CPE Dictionary Files to include the Official CPE 2.2 and 2.3 Dictionary.zip and.gz
	Any organizations making use of the legacy feed files will need to update their systems to use the 2.0 APIs or the 2.0 data feed files.

### July 24, 2025: NVD Technical Update

We plan to deploy updates to NVD systems on July 24th 2025. This deployment includes the following relevant changes:

- **Vulnerability Search:** The NVD Vulnerability Search Page has been redesigned, along with improved filtering and searching capabilities.
	- Accessing vulnerability search results via the old URL path vuln/search/results with query parameters will now redirect to the new main page: `https://nvd.nist.gov/vuln/search#/nvd/home?resultType=records`.
		- Accessing the old "statistics" results via the old URL path vuln/search/statistics will now redirect to `https://nvd.nist.gov/vuln/search#/nvd/home?resultType=statistics`
- **Vulnerability Dashboard Statistics Page:** Total counts have been corrected to reflect adjustments in New CVEs Received by NVD along with corresponding updates to CVEs Undergoing Analysis.
- **Vulnerability (/cves/) API:** Added new parameters related to CISA KEV
	- KevStartDate and kevEndDate return CVEs that were added to the CISA Known Exploited Vulnerabilities (KEV) catalog during a specific period. If a CVE was added to the KEV catalog outside of the specified window, it will not be included.
		- For additional details, please visit the [/cves/ parameter documentation](https://nvd.nist.gov/developers/vulnerabilities).
- We have iterated the [/cves/ schema to version 2.2.3](https://csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema) to align the \`url\` definition with the CVE 5.1.x schema:
	- Removed:
		- `"pattern": "^(ftp|http)s?://\S+$"`
		- Added:
		- `"format": "uri"`
				- `"minLength": 1`
		- Changed:
		- `"maxLength": 2048` (was 500)
- **Legacy Data Feed Reminder:** The following unsupported legacy data feed files will remain available in parallel of the updated 2.0 data feed files until August 20th, 2025 as a courtesy. After that time, the legacy data feed files will be removed from the data feeds page and will no longer be accessible.
	- The  [1.1 Vulnerability Feeds](https://nvd.nist.gov/vuln/data-feeds#JSON_FEED)
		- The  [1.0 CPE Match Feed](https://nvd.nist.gov/vuln/data-feeds#cpeMatch)
		- The Official CPE 2.3 Dictionary [.zip](https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.zip)  and [.gz](https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.gz)
	Any organizations making use of the legacy feed files will need to update their systems to use the 2.0 APIs or the 2.0 data feed files.

### May 19, 2025: NVD Technical Update

We plan to deploy updates to NVD systems the week of May 19, 2025. This deployment includes the following relevant changes:

- **Legacy Data Feed Files Update**
	As stated in the [**February 24, 2025**](https://www.nist.gov/itl/nvd#february2425) Technical Update, we will be providing data feed files that reflect the 2.0 /cves/, /cpematch/ and /cpes/ API response content. These new data feed files will be made available at [https://nvd.nist.gov/vuln/data-feeds#divJson20Feeds](https://nvd.nist.gov/vuln/data-feeds#divJson20Feeds).
	The 2.0 vulnerability feeds follow the same approach as the previous 1.1 vulnerability feed files. They are broken out by “year” and accompanied by the “Recent” and “Modified” feed files.
	Due to the volume of data within the CPE Match 2.0 and CPE Dictionary 2.0 files, the content has been broken into smaller “chunks”. Each chunk should be schema valid and reflect the same structure and formatting as the 2.0 API responses. Additionally, the CPE Match 2.0 and CPE Dictionary 2.0 are provided as tar.gz instead of.gz files.
	The following unsupported legacy data feed files will remain available in parallel until August 20th, 2025 as a courtesy. After that time, the legacy data feed files will be removed from the data feeds page and will no longer be accessible.
	- The [1.1 Vulnerability Feeds](https://nvd.nist.gov/vuln/data-feeds#JSON_FEED)
		- The [1.0 CPE Match Feed](https://nvd.nist.gov/vuln/data-feeds#cpeMatch)
		- The Official CPE 2.3 Dictionary [.zip](https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.zip) and [.gz](https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.gz)
	Any organizations making use of the legacy feed files will need to update their systems to use the 2.0 APIs or the 2.0 data feed files.
	**Looking Ahead...**
	**Network Services Migration**
	NVD infrastructure will be migrating network services. We intend to migrate in a phased approach. Beginning with the website, other services and then the APIs. As part of this transition, users will notice that requests being rate limited will now provide a status code of 429 instead of a status code of 403 “Forbidden by Administrative Rules”.

### April 2, 2025: NVD General Announcement

*(Note: this statement was updated on April 10, 2025 to clarify which CVEs will be deferred.)*

All CVEs with a published date prior to 01/01/2018 that are awaiting further enrichment will be marked as Deferred within the NVD dataset.

We are assigning this status to older CVEs to indicate that we do not plan to prioritize updating their enrichment data due to the CVE’s age.

CVEs marked as Deferred will display a banner on their CVE Detail Pages indicating this status.

This change will take place over the span of several nights. We are doing this to provide additional clarity regarding which CVE records are prioritized.

We will continue to accept and review requests to update the metadata provided for these CVE records. Should any new information clearly indicate that an update to the enrichment data for the CVE is appropriate, we will continue to prioritize those requests as time and resources allow.

In addition, we will prioritize any CVEs that are added to the KEV regardless of status.

### March 19, 2025: NVD General Update

This update provides information on our progress as we work to process incoming CVEs and to address the backlog of CVEs that have not been fully processed:

- We are currently processing incoming CVEs at roughly the rate we had sustained prior to the processing slowdown in spring and early summer of 2024. However, CVE submissions increased 32 percent in 2024, and that prior processing rate is no longer sufficient to keep up with incoming submissions. As a result, the backlog is still growing.
	- We anticipate that the rate of submissions will continue to increase in 2025. The fact that vulnerabilities are increasing means that the NVD is more important than ever in protecting our nation’s infrastructure. However, it also points to increasing challenges ahead.
		To address these challenges, we are working to increase efficiency by improving our internal processes, and we are exploring the use of machine learning to automate certain processing tasks.

### March 11, 2025: NVD Technical Update

*Attention Vulnerability API users that utilize parameters lastModStartDate and lastModEndDate:*

Due to an internal issue with processing analyzed CVEs, please reset your lastModStartDate to ‘2025-02-26T00:00:00.000’. This will ensure all CVE updates are applied appropriately in your environment. We apologize for the inconvenience.

### February 24, 2025: NVD Technical Update

We plan to deploy updates to NVD systems the week of February 24, 2025. This deployment includes the following relevant changes:

- **2.0 API Changes**
	- The [/cves/ schema](https://csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema) has been updated to version 2.2.2
		- Removed the minItems and maxItems restrictions from #definitions/cve\_item/properties/references
		- Resolved incongruent CVSS v4.0 property labels within the JSON responses
		- Implemented multiple performance and stability improvements to the infrastructure and workflows supporting the APIs.

**Looking Ahead...**

- **Legacy Data Feed Files Update**
	We are planning to retire and replace the following legacy data feed files with complimentary data feed files that reflect the 2.0 /cves/, /cpematch/ and /cpes/ API response content.
	- The [1.1 Vulnerability Feeds](https://nvd.nist.gov/vuln/data-feeds#JSON_FEED) with /cves/ 2.0 compliant files.
		- The [1.0 CPE Match Feed](https://nvd.nist.gov/vuln/data-feeds#cpeMatch) with a /cpematch/ 2.0 compliant file.
		- The Official CPE 2.3 Dictionary [.zip](https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.gz) and [.gz](https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.zip) with /cpes/ 2.0 compliant files.
	While we originally intended to move away from supporting this type of bulk download capability, circumstances have redirected our efforts from other, preferred approaches.
	Once these updates are made available, the unsupported legacy data feed files will remain available in parallel for 3 months as a courtesy. After that time, the legacy 1.1 feed files will no longer be accessible. Any organizations making use of the legacy feed files will need to update their systems to use the 2.0 APIs or the 2.0 data feed files.
