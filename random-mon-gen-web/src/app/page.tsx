import Image from 'next/image';

async function getRandomPokemon() {
  const res = await fetch('http://localhost:3000/api/random-pokemon', {
    cache: 'no-store', // Verhindert Caching, um jedes Mal ein neues Pokémon zu bekommen
  });

  if (!res.ok) {
    throw new Error('Failed to fetch Pokémon');
  }

  return res.json();
}

export default async function Home() {
  const pokemon = await getRandomPokemon();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-3xl font-bold mb-4">{pokemon.name}</h1>
      <div className="bg-white p-6 rounded-lg shadow-lg">
        <Image
          src={`/Pokemon_sprites/${pokemon.id}.png`} // Pfad zum Bild
          alt={pokemon.name}
          width={200}
          height={200}
          className="mb-4"
        />
        <p><strong>Typ 1:</strong> {pokemon.type1}</p>
        <p><strong>Typ 2:</strong> {pokemon.type2 || 'N/A'}</p>
        <p><strong>Generation:</strong> {pokemon.generation}</p>
      </div>
    </div>
  );
}