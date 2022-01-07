# TestingAutomation

Your task is to write an automated test for the GitHub search in Python. We are using multiple filters to
find this repository: [https://github.com/mvoloskov/decider](https://github.com/mvoloskov/decider).
Here's a rough scenario
1. Open [https://github.com/](https://github.com/).
2. Focus the `Search GitHub` search bar.
3. Input `react` and submit.
4. In the search results, find `Advanced Search` and click it.
5. Set the following parameters for the search:
- Written in this language: JavaScript;
- With this many stars: >45;
- With this many followers: >50;
- With this license: Boost Software License 1.0;
6. Press search.
7. Verify that there is only `1 repository result`.
8. Verify that the result list includes this repository: `mvoloskov/decider`.
9. Navigate to the repository page.
10. Print the first 300 characters of the `[README.md](http://readme.md/)`.
