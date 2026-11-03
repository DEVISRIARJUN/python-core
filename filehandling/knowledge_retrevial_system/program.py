
# STEP 1: Read the knowledge file line by line
with open("knowledge.txt", "r") as f:
    lines = []

    for line in f:
        lines.append(line.strip())


# STEP 2: Combine every 2 lines into 1 chunk
chunks = []

i = 0
while i < len(lines):
    if i + 1 < len(lines):
        chunk = lines[i] + " " + lines[i + 1]
    else:
        # If one line remains, store it as a separate chunk
        chunk = lines[i]

    chunks.append(chunk)
    i += 2


# STEP 3: Write all chunks into vector_store.txt
with open("vector_store.txt", "w") as f:
    for chunk in chunks:
        f.write(chunk + "\n")


# STEP 4: Ask the user for repeated queries
while True:
    query = input("\nEnter your query (or type exit): ")

    if query.lower() == "exit":
        print("Exiting the retrieval system...")
        break

    # Convert the query into lowercase words
    query_words = query.lower().split()

    # STEP 5: Compare query words with each chunk
    highest_score = 0
    best_chunk = ""

    with open("vector_store.txt", "r") as f:

        # Use seek() to move the file cursor to the beginning
        f.seek(0)

        for chunk in f:
            chunk = chunk.strip()
            chunk_words = chunk.lower().split()

            # Count how many query words match the chunk
            score = 0

            for word in query_words:
                if word in chunk_words:
                    score += 1

            # STEP 6: Keep the chunk with the highest score
            if score > highest_score:
                highest_score = score
                best_chunk = chunk

    # Display the best matching chunk
    if highest_score > 0:
        print("\nBest matching chunk:")
        print(best_chunk)
        print("Matching score:", highest_score)
    else:
        print("\nNo matching information found.")
