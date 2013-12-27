import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--resolution", default="1024x768", help="background resoltion; default 1024x768")
parser.add_argument("-b", "--background", default="#152233", help="plot background color; default #152233, use \# in your shell")
parser.add_argument("-s", "--samplesize", type=int,  default=7, help="number of samples to draw from prior; default 7")
parser.add_argument("-o", "--output", help="output file path, name and type (png, pdf, ps, eps and svg); default displays plot")
args = parser.parse_args()

N = 100
samples = args.samplesize

width_in = 10.0
width_px = int(args.resolution.split('x')[0])
height_px = int(args.resolution.split('x')[1])
aspect = width_px / float(height_px)
height_in = width_in / aspect
dpi = width_px / width_in
fig = plt.figure(figsize=(width_in, height_in), facecolor=args.background)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

x = np.linspace(0, 5, N)
K = np.zeros((N, N))
for xi in range(0, N):
	for xj in range(0, N):
		K[xj][xi] = np.exp(-1/2*(x[xi]-x[xj])**2)

L = np.linalg.cholesky(K+1e-6*np.eye(N))
L = np.transpose(L)
f = np.zeros((samples, N))
for k in range(0, samples):
	f[k] = np.dot(np.random.randn(1, N),L)
	ax.plot(x, f[k], linewidth=2.0, antialiased=True)

if args.output == None:
    plt.show()
else:
    plt.savefig(args.output, dpi=dpi, facecolor=args.background)