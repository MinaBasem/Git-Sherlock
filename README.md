## 🕵️‍♀️ GitSherlock: Your GitHub Repository Sleuth 🕵️‍♀️

**GitSherlock** is your one-stop shop for analyzing and understanding GitHub repositories! 💥 It's like a super-powered magnifying glass for code, allowing you to dive deep into any repository's structure, content, and functionality. 🔭

### ⚡ What can GitSherlock do? ⚡

* **Validate GitHub repository URLs:**  Ensure you're looking at the right codebase! 🔐
* **Summarize the repository:** No need to read the entire README, GitSherlock will do that for you. 😉
* **Generate a file tree:**  Visually explore the repository's directory structure. 🌳
* **Analyze individual files:**  Get descriptions and function breakdowns for supported file types (including Python, JavaScript, Java, C++, and more!). 🧠
* **Display repository details:**  Get important information like the owner, number of stars, forks, open issues, and language. ✨
* **Interactive mode:**  Analyze multiple repositories without leaving the terminal! 💻

### ✨ How to Use GitSherlock ✨

1. **Install Python:** Make sure you have Python installed on your system.
2. **Install GitSherlock:**
    ```bash
   pip install git-sherlock 
   ```
3. **Setup up the environment variable for Gemini API key:**
  - For Linux:
    ```export GEMINI_API_KEY=XXXXXXXXX```
  - For Windows:
    ```set GEMINI_API_KEY=XXXXXXXXX```
4. **Run GitSherlock:** 
   ```bash
   git-sherlock -u <github_repository_url>
   ```
   Or, use the interactive mode:
   ```bash
   git-sherlock -i 
   ```

### Example Usage 🚀

```bash
git-sherlock -u https://github.com/facebook/react
```

This command will analyze the React repository and display the following:

* A summary of the README file.
* A detailed file tree showing the repository's structure.
* Analysis of each supported file, including descriptions and functions.
* Repository details like owner, stars, forks, etc.

### Features You'll Love 🎉

* **Rich Terminal Output:**  Enjoy beautiful and informative output with colors and formatting! 🌈
* **User-Friendly:**  Easy to use, even if you're new to analyzing code. 🧑‍💻
* **Fast and Efficient:**  Get your analysis results quickly and effortlessly. ⚡️
* **Constantly Evolving:**  There's more to be added to the experience. 🚀

### Contributions

Like the project and think you have room for improving it? Don't hesitate to send in a Pull Request

---

**Ready to unravel the mysteries of GitHub repositories?  Install GitSherlock and start exploring!** 😎
