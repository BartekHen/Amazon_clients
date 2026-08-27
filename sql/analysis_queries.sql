-- Example analytical queries over the reviews table.
-- Run with:
--   duckdb reviews.duckdb < sql/analysis_queries.sql


-- 1. Average sentiment score by rating label (1 = negative, 2 = positive).
SELECT
    rating,
    ROUND(AVG(sentiment_score), 3) AS avg_sentiment,
    COUNT(*) AS review_count
FROM reviews
GROUP BY rating
ORDER BY rating;


-- 2. Reviews where the label and the sentiment disagree the most -
-- e.g. a "positive" review that reads very negative, or the other way round.
SELECT
    rating,
    sentiment_score,
    LEFT(clean_review, 120) AS review_preview
FROM reviews
WHERE (rating = 2 AND sentiment_score < -0.3)
   OR (rating = 1 AND sentiment_score > 0.3)
ORDER BY ABS(sentiment_score) DESC
LIMIT 10;


-- 3. Average exclamation mark usage: negative vs. positive reviews.
SELECT
    rating,
    ROUND(AVG(exclamation_count), 2) AS avg_exclamations
FROM reviews
GROUP BY rating
ORDER BY rating;


-- 4. Review length distribution by rating, bucketed into short/medium/long.
SELECT
    rating,
    CASE
        WHEN word_count < 50 THEN 'short (<50 words)'
        WHEN word_count < 150 THEN 'medium (50-150 words)'
        ELSE 'long (150+ words)'
    END AS length_bucket,
    COUNT(*) AS review_count
FROM reviews
GROUP BY rating, length_bucket
ORDER BY rating, length_bucket;
