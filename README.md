# resample

Downsampling is implemented through matrix transformation, where the value of each downsampled pixel equals the average of the corresponding source pixels.
Specifically:
If the original image has a size of n × m and is downsampled to p × q (with n > p, m > q), then each pixel in the downsampled image corresponds to the mean of a (n/p) * (m/q) block in the original image.
For example：
original image with size of 5*5, downsampled image with size of 4*2, then the transformation will be like:
downsampled image = $$
 \left[
 \begin{matrix}
   1 & 2 & 3 \\
   4 & 5 & 6 \\
   7 & 8 & 9
  \end{matrix}
  \right] \tag{3}
$$
