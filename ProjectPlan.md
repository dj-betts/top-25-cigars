# Cigar Recommender Engine Project Plan

## Project Goal
##### *Create a recommender engine that uses tasting notes to suggest cigars with similar profiles, with a roadmap for iterative enhancements incorporating additional features.*

---

## Phase 1: Project Setup and Data Preparation
1. **Define Requirements and Success Metrics**
   - Set performance goals for the recommender system, e.g., precision/recall of recommendations or user satisfaction.
   - Choose a dataset split (e.g., train-test split) for model evaluation.

2. **Data Cleaning and Preprocessing**
   - **Text Cleaning**: Clean up `tasting_notes` to remove extraneous symbols, whitespace, or encoding issues.
   - **Tokenization and Lemmatization**: Tokenize the tasting notes and reduce words to their base forms to enhance pattern recognition.
   - **Handle Missing Values**: Address any missing entries in key columns (`tasting_notes`, `score`, etc.).

---

## Phase 2: Build Initial NLP-Based Recommender Engine
1. **Vectorize Tasting Notes**
   - Experiment with vectorization techniques like TF-IDF or Word2Vec embeddings for the `tasting_notes` text to capture semantic similarity.

2. **Similarity Calculation**
   - **Similarity Measures**: Use cosine similarity or another metric to find cigars with the closest tasting notes.
   - Implement a basic function that, given a cigar name, returns a list of the top-N similar cigars.

3. **Evaluate Initial Recommendations**
   - Conduct a qualitative assessment of recommendations by manually reviewing similar cigar suggestions.
   - (Optional) Gather user feedback on similarity quality if available.

---

## Phase 3: Incorporate Additional Features for Enhanced Recommendations
1. **Feature Engineering**
   - **Numeric Features**: Include `score`, `length`, and `gauge` for refining recommendations.
   - **Categorical Features**: Add `strength`, `size`, and `country` as features. Use one-hot encoding or embedding for categorical variables.
   - **Price**: Normalize or categorize price to account for budget-based recommendations.

2. **Hybrid Recommendation System**
   - Combine NLP-derived tasting note similarity with additional features (e.g., weighted hybrid system).
   - Experiment with different weightings and distances to find an optimal balance.

3. **Evaluate Enhanced Recommender**
   - Use cross-validation to test performance with additional features.
   - If possible, measure accuracy or satisfaction through user testing or historical review data.

---

## Phase 4: Refine, Deploy, and Monitor
1. **Optimize and Fine-Tune**
   - Hyperparameter tuning for the similarity model and feature weights.
   - Explore dimensionality reduction on feature vectors (e.g., PCA or t-SNE) for faster computations if necessary.

2. **Deployment Preparation**
   - Package the model into a deployable format (e.g., Flask API or a standalone script).
   - Implement a simple UI to test the recommender or provide recommendations via a command-line interface.

3. **Ongoing Monitoring and Updates**
   - Set up a system to periodically refresh the model as new data arrives (e.g., new cigar reviews).
   - Track system performance metrics and retrain the model as necessary.

---

## Future Enhancements (Optional)
- **User Feedback Integration**: Include user ratings to improve personalized recommendations.
- **Content-Based Filtering**: Integrate with collaborative filtering techniques if user purchase data becomes available.
- **Advanced NLP**: Experiment with transformer-based models (like BERT) on tasting notes for potentially improved similarity capture.

---