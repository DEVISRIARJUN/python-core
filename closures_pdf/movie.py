# Question 5

# Write a function movie(movie_name).

# -   The outer function stores the movie name.
# -   The inner function receives the person’s name.
# -   Print that the person booked a ticket for the movie.
# -   Return the inner function.

def movie(movie_name):
    def person(name):
        return f"{name} booked a ticket for the {movie_name} movie"
    return person
c = movie("Kanchana")
print(c("Arjun"))