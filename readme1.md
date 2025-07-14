# resample

Downsampling is implemented through matrix transformation, where the value of each downsampled pixel equals the average of the corresponding source pixels.

Specifically, if the original image has a size of **n × m** and is downsampled to **p × q** (with **n > p**, **m > q**), then each pixel in the downsampled image corresponds to the mean of a **(n/p) × (m/q)** block in the original image.

### Example

If the original image (O) has a size of **5 × 5**, and the target downsampled image (D) is **4 × 2**, the transformation process would look like this:

$D=L \cdot O \cdot R$

$$
L=\left[
\begin{matrix}
1 & 0.25 & \ & \\
 \  & 0.75 & 0.5 &  \ \\
 \  &  \  & 0.5 & 0.75 &  \ \\
 \  &  \  & \ & 0.25 &  1 & \ \\
\end{matrix}
\right], \
R=\left[
\begin{matrix}
1 & \ \\
1 & \ \\
0.5 & 0.5 \\
\ & 1 \\
\ & 1 \\
\end{matrix}
\right]
$$