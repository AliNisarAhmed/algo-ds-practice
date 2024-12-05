function floodFill(
  image: number[][],
  sr: number,
  sc: number,
  newColor: number,
): number[][] {
  const color = image[sr][sc];
  if (color !== newColor) {
    dfs(image, sr, sc, color, newColor);
  }
  return image;
}

function dfs(
  image: number[][],
  sr: number,
  sc: number,
  currentColor: number,
  newColor: number,
) {
  if (image[sr][sc] === currentColor) {
    image[sr][sc] = newColor;

    if (sr >= 1) {
      dfs(image, sr - 1, sc, currentColor, newColor);
    }

    if (sc >= 1) {
      dfs(image, sr, sc - 1, currentColor, newColor);
    }

    if (sr <= image.length) {
      dfs(image, sr + 1, sc, currentColor, newColor);
    }

    if (sc <= image[0].length) {
      dfs(image, sr, sc + 1, currentColor, newColor);
    }
  }
}
