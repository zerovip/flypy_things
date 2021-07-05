# flypy_things
Some things about [flypy](https://flypy.com/), which is a Chinese input method scheme.

There are five files in this repo. By the followong order, they are for:

- `flypy.json`: Original data got from [here](http://react.xhup.club/search). [8105 characters](https://github.com/rime-aca/character_set/blob/master/通用規範漢字表.txt) in total.
- `reformat.py`: A script to reformat the original data into a prettier one.
- `flypy_n.json`: The prettier format of the same 8105 characters data. Also accessible on [gist (size: 1.6 M)](https://gist.github.com/zerovip/5e5228fecdf121a956386c69cb3ee0c2).
- `analyze.py`: A script to analyze the flypy code.
- `result.json`: The results of previous analysis, includings all the items I am particularly interested in. [More details (in Chinese)]( https://zerovip.github.io/zh/95251/).
