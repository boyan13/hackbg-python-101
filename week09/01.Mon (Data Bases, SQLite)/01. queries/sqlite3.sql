ALTER TABLE languages
  ADD COLUMN rating CHECK (rating BETWEEN 1 AND 9);
