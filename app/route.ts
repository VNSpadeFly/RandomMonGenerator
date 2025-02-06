import { Pool } from 'pg';
import { NextResponse } from 'next/server';

const pool = new Pool({
  user: 'postgres', // Standardmäßig oft 'postgres'
  host: 'localhost',         // Da die DB lokal läuft
  database: 'RandomMonGenerator', // Name deiner Datenbank
  password: 'password', // Passwort für deine PostgreSQL-DB
  port: 5433,                // Standard-Port für PostgreSQL
});

export async function GET() {
  try {
    const { rows } = await pool.query('SELECT * FROM pokemon ORDER BY RANDOM() LIMIT 1');
    return NextResponse.json(rows[0]);
  } catch (error) {
    console.error('Fehler beim Abrufen des Pokémon:', error);
    return NextResponse.json({ error: 'Failed to fetch Pokémon' }, { status: 500 });
  }
}