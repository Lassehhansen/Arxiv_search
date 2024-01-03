# Arxiv_search

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
