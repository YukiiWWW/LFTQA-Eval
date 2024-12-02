## LfTQA-Eval
The data and code for the EMNLP 2024 short paper [Revisiting Automated Evaluation for Long-form Table Question Answering](https://aclanthology.org/2024.emnlp-main.815.pdf). 
**LfTQA-Eval** is a meta-evaluation dataset containing 2,988 human-annotated examples, designed to rigorously evaluate the performance of current automated metrics in assessing LLM-based LFTQA systems, with an emphasis on faithfulness and comprehensiveness.

### LfTQA-Eval Dataset
- The outputs of different LLMs on the FeTaQA and QTSumm datasets are provided in `model_outputs.json`
- The human-annotated scores are provided in 
  - `scores/fetaqa/human_scores` for the FeTaQA dataset
  - `scores/qtsumm/human_scores` for the QTSumm dataset
- The automated scores are provided in 
  - `scores/fetaqa/metric_scores` for the FeTaQA dataset
  - `scores/qtsumm/metric_scores` for the QTSumm dataset

### Experiments
For calculating the correlation scores reported in the paper, please run the following command:
```bash
python calculate_correlation.py
```
The results will be saved in `correlation_results.csv`.

**Important Note**: There is an error in the header of Table 2 in the original manuscript. The column headers are mistakenly swapped in the published paper. The correct order of the headers should be: "Comprehensiveness-FeTaQA", "Comprehensiveness-QTSumm", "Faithfulness-QTSumm", "Faithfulness-FeTaQA" instead of the published order: "FeTaQA-Comp.", "FeTaQA-Faith.", "QTSumm-Comp.", "QTSumm-Faith.".

### Contact
For any issues or questions, kindly email us at: Yuqi Wang (yuqiw0099@gmail.com).

### Citation
If you use our benchmark in your work, please kindly cite the paper:

```
@inproceedings{wang-etal-2024-revisiting,
    title = "Revisiting Automated Evaluation for Long-form Table Question Answering",
    author = "Wang, Yuqi  and
      Chen, Lyuhao  and
      Cai, Songcheng  and
      Xu, Zhijian  and
      Zhao, Yilun",
    editor = "Al-Onaizan, Yaser  and
      Bansal, Mohit  and
      Chen, Yun-Nung",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.emnlp-main.815",
    doi = "10.18653/v1/2024.emnlp-main.815",
    pages = "14696--14706",
    abstract = "In the era of data-driven decision-making, Long-Form Table Question Answering (LFTQA) is essential for integrating structured data with complex reasoning. Despite recent advancements in Large Language Models (LLMs) for LFTQA, evaluating their effectiveness remains a significant challenge. We introduce LFTQA-Eval, a meta-evaluation dataset comprising 2,988 human-annotated examples, to rigorously assess the efficacy of current automated metrics in assessing LLM-based LFTQA systems, with a focus on faithfulness and comprehensiveness. Our findings reveal that existing automatic metrics poorly correlate with human judgments and fail to consistently differentiate between factually accurate responses and those that are coherent but factually incorrect. Additionally, our in-depth examination of the limitations associated with automated evaluation methods provides essential insights for the improvement of LFTQA automated evaluation.",
}
```