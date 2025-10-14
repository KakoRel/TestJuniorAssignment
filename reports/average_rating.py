def average_rating(rows):
    """Вычисляет средний рейтинг по каждому бренду."""
    brands = {}
    counts = {}

    for row in rows:
        brand = row.get("brand", "").strip()
        rating = row.get("rating", "").strip()

        if not brand:
            continue
        try:
            rating = float(rating)
        except ValueError:
            continue

        brands[brand] = brands.get(brand, 0) + rating
        counts[brand] = counts.get(brand, 0) + 1

    results = []
    for brand in brands:
        avg = round(brands[brand] / counts[brand], 2)
        results.append([brand, avg])

    results.sort(key=lambda x: (-x[1], x[0]))
    return results
