# (Re)Imagining Price Trends: A Replication Study

This project is a replication of the methodology introduced in the paper *(Re-)Imag(in)ing Price Trends* by Kelly et al. The study explores machine learning techniques to detect complex price patterns that traditional finance methods might miss. Specifically, the methodology uses convolutional neural networks (CNNs) trained on price chart images to predict stock returns and create portfolios.

## Overview

The project involves the following steps:

1. **Data Collection**: Daily stock price data for S&P 500 companies from 2010 to 2024.
2. **Image Generation**: Converting price and volume data into chart images with additional indicators like moving averages.
3. **Model Training**: Using CNNs to predict the probability of positive returns.
4. **Portfolio Construction**: Developing long-short and long-only strategies based on the model's predictions.
5. **Evaluation**: Comparing model-based portfolios to benchmarks like random portfolios, uniform portfolios, and the S&P 500 index.

## File Structure

- `1) DownloadData.ipynb`: Fetches and preprocesses the stock price data.
- `2) ImageGeneration.ipynb`: Converts price data into images.
- `3) CNN5day.ipynb`, `4) CNN20day.ipynb`, `5) CNN60day.ipynb`: Train CNN models for 5-day, 20-day, and 60-day prediction horizons.
- `6) OutOfSampleEvaluation5day.ipynb`: Evaluate the 5-day model on the test dataset.
- `7) OutOfSampleEvaluation20day.ipynb`: Evaluate the 5-day model on the test dataset.
- `8) OutOfSampleEvaluation60day.ipynb`: Evaluate the 5-day model on the test dataset.
- `h) Random and Uniform.ipynb`: Analyze random and uniform portfolio benchmarks.
- `h) SP500.ipynb`: Analyze the S&P 500 as a benchmark.
- `data/`: Directory for storing raw and processed data.
- `models/`: Directory for storing trained models.
- `utils/`: Utility classes.
- `Project_presentation.pdf`: Slides for the in class presentation

## Results

- The 5-day CNN model outperformed benchmarks with an overall return of 65.16% and an average yearly return of 13.98% (long-only strategy).
- Longer prediction horizons (20-day, 60-day) had diminishing returns.
- Detailed results and comparisons can be found in `Project_presentation.pdf`.

## References
Kelly, B., Pruitt, S., & Su, Y. (2023). (Re-)imag(in)ing Price Trends. Journal of Financial Economics, [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3756587].

## License

This project is proprietary, and all rights are reserved. Any use, modification, or distribution of this work is prohibited without explicit permission from the authors. For inquiries, please contact [fabio190901@gmail.com].
