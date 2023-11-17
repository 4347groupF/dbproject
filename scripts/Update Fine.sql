-- Script attached to a cron job that will run daily
-- Update books returned late

INSERT INTO FINES (loan_id, fine_amt)
SELECT loan_id, 0.25 * DATEDIFF(date_in, due_date) as fine
FROM BOOK_LOANS 
WHERE date_in > due_date
ON DUPLICATE KEY UPDATE
fine_amt = 0.25 * DATEDIFF(date_in, due_date);

-- Update books that are still out

INSERT INTO FINES (loan_id, fine_amt)
SELECT loan_id, 0.25 * DATEDIFF(CURDATE(), due_date) as fine
FROM BOOK_LOANS 
WHERE date_in IS NULL AND CURDATE() > due_date
ON DUPLICATE KEY UPDATE
fine_amt = 0.25 * DATEDIFF(CURDATE(), due_date);