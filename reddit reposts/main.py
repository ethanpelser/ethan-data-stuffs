from Image_Comparer import compare
from Image_Scraper import scraper
from Image_Sorter import sorter

Reddit = input("Enter your desired subreddit -")
amount = input("Enter the amount of posts to go through required -")


numba = int(amount)


scraper(numba, Reddit)
sorter()
compare()

print("it is done")
