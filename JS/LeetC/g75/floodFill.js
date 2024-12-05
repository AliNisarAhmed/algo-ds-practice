function floodFill(image, sr, sc, color) {
  let startingColor = image[sr][sc];

  if (startingColor !== color) {
    floodFillRec(image, sr, sc, color, startingColor);
  }

  return image;
}

function floodFillRec(image, sr, sc, targetColor, startingColor) {
  if (image[sr][sc] === startingColor) {
    image[sr][sc] = targetColor;

    if (sr >= 1) {
      floodFillRec(image, sr - 1, sc, targetColor, startingColor);
    }

    if (sr + 1 < image.length) {
      floodFillRec(image, sr + 1, sc, targetColor, startingColor);
    }

    if (sc >= 1) {
      floodFillRec(image, sr, sc - 1, targetColor, startingColor);
    }

    if (sc + 1 < image[0].length) {
      floodFillRec(image, sr, sc + 1, targetColor, startingColor);
    }
  }

}

console.log(
  floodFill(
    [
      [1, 1, 1],
      [1, 1, 0],
      [1, 0, 1],
    ],
    1,
    1,
    2,
  ),
);
