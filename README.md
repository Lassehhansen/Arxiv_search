# Arxiv Search

## Downloading the Arxiv Dataset:

Detailed documentation for the download can be found [here](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T).

To download only the files used for the litterature search, follow these steps: 

```bash
# Download the urls.txt file which contains URLs to all the datasets
wget 'https://data.together.xyz/redpajama-data-1T/v1.0.0/urls.txt'

# Get the urls related to each of the datasets in RedPajama
grep “arxiv” urls.txt > arxiv_urls.txt

# Use the modified script to download only the specific files
while read line; do
    dload_loc=${line#https://data.together.xyz/redpajama-data-1T/v1.0.0/}
    mkdir -p $(dirname $dload_loc)
    wget "$line" -O "$dload_loc"
done < arxiv_urls.txt
```

## Dataset description

- 88 GB
- Total number of texts in JSONL files: 1558306
- Total number of texts that contain either AUROC OR AUPRC related keywords: 16022
- Total number of texts that contain both: 8244
- Texts after GPT 3.5 search: 2728
- Texts after GPT 4.0 Turbo search (only 73% scanned): 197

## Keyword Filtering

1.  **Creation of Keyword Lists:** Two separate lists of keywords were created for AUROC and AUPRC, respectively. These lists are crucial in identifying relevant papers in the Arxiv dataset. You can find the keyword lists [here for AUPRC](https://github.com/Lassehhansen/Arxiv_search/blob/main/keyword_lists/keywords_auprc.py) and [here for AUROC](https://github.com/Lassehhansen/Arxiv_search/blob/main/keyword_lists/keywords_auroc.py).
    
2.  **Script-Driven Search:** We used Python scripts to automate the search through the Arxiv dataset. The scripts scanned the texts for occurrences of the keywords from both lists.
    
3.  **Dual Mention Filtering:** Papers that mentioned both AUROC and AUPRC were specifically filtered to ensure relevance to our research question. This resulted in 8,244 papers from the initial 16,022 that contained either set of keywords.
    

## AI-Assisted Review

1.  **Initial Screening with GPT-3.5:** The first round of AI-assisted review utilized OpenAI's GPT-3.5 model. The model was prompted to identify papers that explicitly made claims about the superiority of AUPRC over AUROC in cases of class imbalance. This process reduced the number of relevant papers to 2,728.
    
2.  **Further Refinement with GPT-4.0 Turbo:** A more advanced review was conducted using GPT-4.0 Turbo. At the time of this documentation, approximately 73% of the 2,728 papers have been scanned, leading to the identification of 197 papers that are highly relevant to our research focus.
    

## Data Sharing and Collaborative Review

*   **Google Docs for Collaboration:** All identified papers, along with their respective Arxiv IDs and the claims found by GPT-4.0 Turbo, have been compiled in a shared Google document for collaborative review and analysis. \[Access the shared document here\](LINK HERE).
*   **Color-Coding for Agreement:** Team members were encouraged to review the listed papers and color-code them based on their alignment with our research focus: green for papers supporting our interest points and red for those that do not align.

### Continuous Updates

*   **Ongoing Analysis:** The review process is ongoing, and the document will be updated as more papers are analyzed. Team members are encouraged to contribute by adding new findings or adjusting existing ones.
*   **Progress Tracking:** The current status of the analysis, including the number of papers reviewed and the insights gained, will be regularly updated in this README.

