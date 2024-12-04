class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, og = None) -> List[List[int]]:
        x_length = len(image)
        y_length = len(image[0])

        if sr < 0 or sc < 0 or sr >= x_length or sc >= y_length:
            return image

        if og is None and image[sr][sc] != color:
            og = image[sr][sc]
            print(og)

        if image[sr][sc] == og:
            image[sr][sc] = color
            image = self.floodFill(image, sr-1, sc, color, og)
            image = self.floodFill(image, sr, sc-1, color, og)
            image = self.floodFill(image, sr+1, sc, color, og)
            image = self.floodFill(image, sr, sc+1, color, og)

        return image
