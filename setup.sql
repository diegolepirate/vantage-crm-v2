-- Run this in Supabase SQL Editor

-- Create prospects table
CREATE TABLE IF NOT EXISTS prospects (
  id SERIAL PRIMARY KEY,
  nom TEXT NOT NULL,
  numero TEXT,
  type_tel TEXT DEFAULT 'Fixe',
  famille TEXT DEFAULT 'Autre',
  categorie TEXT,
  region TEXT DEFAULT 'Grece',
  adresse TEXT,
  rating TEXT,
  avis TEXT,
  vendeur TEXT DEFAULT '',
  status TEXT DEFAULT 'nouveau',
  notes TEXT DEFAULT '',
  call_date TIMESTAMPTZ,
  revenue NUMERIC DEFAULT 0,
  blacklisted BOOLEAN DEFAULT false,
  total_calls INTEGER DEFAULT 0,
  last_called_at TIMESTAMPTZ,
  call_duration_total INTEGER DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Disable RLS (internal tool, no public access needed)
ALTER TABLE prospects DISABLE ROW LEVEL SECURITY;

-- Create index for fast filtering
CREATE INDEX IF NOT EXISTS idx_prospects_region ON prospects(region);
CREATE INDEX IF NOT EXISTS idx_prospects_famille ON prospects(famille);
CREATE INDEX IF NOT EXISTS idx_prospects_vendeur ON prospects(vendeur);
CREATE INDEX IF NOT EXISTS idx_prospects_status ON prospects(status);
CREATE INDEX IF NOT EXISTS idx_prospects_type_tel ON prospects(type_tel);
