The problem with many available frequency lists is that they don't take word morphologies into account. For example, in English, "playing" and "played" might be found seperated in a frequency list. This code adresses this issue by taking morphology into account. An experiment word list order by frequency is in the "5000.txt" file.

## Example:
The file 5000.txt (in the 'data' folder) contains top 5000 German words ranked by frequency based on German movie subtitles. It only display one form of each group of word morphologies. The list was just generated from the code available here and needs some refinement.

- The data was generated via [LuminosoInsight](https://github.com/LuminosoInsight/wordfreq) and [german-morph-dictionaries](https://github.com/DuyguA/german-morph-dictionaries).
