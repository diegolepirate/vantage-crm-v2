-- ============================================
-- VANTAGE CRM — COMPLETE MIGRATION
-- Run in Supabase SQL Editor
-- ============================================

-- 1. Project Objectives table
CREATE TABLE IF NOT EXISTS project_objectives (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  project_id uuid REFERENCES projects(id) ON DELETE CASCADE,
  type text DEFAULT 'preset',
  description text NOT NULL,
  target_value integer DEFAULT 0,
  current_value integer DEFAULT 0,
  completed boolean DEFAULT false,
  points_reward integer DEFAULT 50,
  vendor text,
  created_at timestamptz DEFAULT now()
);
ALTER TABLE project_objectives ENABLE ROW LEVEL SECURITY;
CREATE POLICY "allow_all_objectives" ON project_objectives FOR ALL USING (true);

-- 2. Missing columns on prospects
ALTER TABLE prospects ADD COLUMN IF NOT EXISTS blacklisted boolean DEFAULT false;
ALTER TABLE prospects ADD COLUMN IF NOT EXISTS total_calls integer DEFAULT 0;
ALTER TABLE prospects ADD COLUMN IF NOT EXISTS last_called_at timestamptz;
ALTER TABLE prospects ADD COLUMN IF NOT EXISTS call_duration_total integer DEFAULT 0;

-- 3. Vendor Badges table (replace localStorage)
CREATE TABLE IF NOT EXISTS vendor_badges (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  vendor_name text NOT NULL,
  badge_id text NOT NULL,
  unlocked_at timestamptz DEFAULT now(),
  UNIQUE(vendor_name, badge_id)
);
ALTER TABLE vendor_badges ENABLE ROW LEVEL SECURITY;
CREATE POLICY "allow_all_badges" ON vendor_badges FOR ALL USING (true);

-- 4. Vendor Stats table (streaks, points)
CREATE TABLE IF NOT EXISTS vendor_stats (
  vendor_name text PRIMARY KEY,
  current_streak integer DEFAULT 0,
  longest_streak integer DEFAULT 0,
  last_call_date date,
  total_points integer DEFAULT 0,
  updated_at timestamptz DEFAULT now()
);
ALTER TABLE vendor_stats ENABLE ROW LEVEL SECURITY;
CREATE POLICY "allow_all_vendor_stats" ON vendor_stats FOR ALL USING (true);

-- 5. RPC: get_distinct_regions (performance fix)
CREATE OR REPLACE FUNCTION get_distinct_regions()
RETURNS TABLE(region text, total bigint) AS $$
SELECT region, COUNT(*) as total FROM prospects
WHERE region IS NOT NULL AND region != ''
GROUP BY region ORDER BY total DESC;
$$ LANGUAGE sql SECURITY DEFINER;

-- 6. RPC: get_owner_counts (performance fix)
CREATE OR REPLACE FUNCTION get_owner_counts(current_vendor text)
RETURNS json AS $$
SELECT json_build_object(
  'all', COUNT(*),
  'free', COUNT(*) FILTER (WHERE vendeur IS NULL OR vendeur = ''),
  'assigned', COUNT(*) FILTER (WHERE vendeur IS NOT NULL AND vendeur != ''),
  'mine', COUNT(*) FILTER (WHERE vendeur = current_vendor)
) FROM prospects WHERE blacklisted IS NOT TRUE;
$$ LANGUAGE sql SECURITY DEFINER;

-- 7. GIN indexes for search performance
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX IF NOT EXISTS idx_prospects_nom_trgm ON prospects USING GIN (nom gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_prospects_numero_trgm ON prospects USING GIN (numero gin_trgm_ops);

-- 8. Update setup.sql indexes
CREATE INDEX IF NOT EXISTS idx_prospects_blacklisted ON prospects(blacklisted);
CREATE INDEX IF NOT EXISTS idx_prospects_total_calls ON prospects(total_calls);
