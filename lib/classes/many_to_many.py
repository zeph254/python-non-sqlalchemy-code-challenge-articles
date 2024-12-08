class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("please provide author name.")
        if not isinstance(magazine, Magazine):
            raise ValueError("please provide magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must have between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine
        self.title = title
        author._articles.append(self)
        magazine._articles.append(self)
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("name must be provided.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    _all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("provide a valid input.")
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all.append(self)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        contributors = {}
        for article in self._articles:
            author = article.author
            contributors[author] = contributors.get(author, 0) + 1
        result = [author for author, count in contributors.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls._all:
            return None
        return max(cls._all, key=lambda mag: len(mag._articles))
    

author1 = Author("John Doe")
author2 = Author("Jane Smith")

mag1 = Magazine("Tech Monthly", "Technology")
mag2 = Magazine("Health Weekly", "Health")

# Adding articles
article1 = author1.add_article(mag1, "life and Future")
article2 = author1.add_article(mag2, "Healthy Living Tips")
article3 = author2.add_article(mag1, "Tech Trends 2024")
article4 = author1.add_article(mag1, "Blockchain Explained")


print(author1.magazines())  
print(mag1.contributors())  
print(mag1.article_titles())  
print(Magazine.top_publisher())  