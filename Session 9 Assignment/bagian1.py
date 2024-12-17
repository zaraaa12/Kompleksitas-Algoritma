def subset_sum_backtrack(array, target):
    result = []

    def backtrack(current_subset, current_sum, index):
        # Kasus dasar: jika jumlah saat ini sama dengan target, tambahkan ke hasil
        if current_sum == target:
            result.append(list(current_subset))
            return

        # Jika jumlah melebihi target atau indeks melampaui panjang array, berhenti
        if current_sum > target or index >= len(array):
            return

        # Tambahkan elemen saat ini ke subset
        current_subset.append(array[index])
        backtrack(current_subset, current_sum + array[index], index)

        # Keluarkan elemen terakhir untuk mencoba kombinasi lain
        current_subset.pop()
        backtrack(current_subset, current_sum, index + 1)

    backtrack([], 0, 0)
    return result

# Contoh masukan
array = [2, 4, 6, 8, 10]
target = 10

# Panggil fungsi dan tampilkan hasil
result = subset_sum_backtrack(array, target)
print("Semua subset yang jumlahnya", target, ":", result)
