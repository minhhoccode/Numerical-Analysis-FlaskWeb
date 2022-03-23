
# @app.route('/visualize')
# def plot_png():
#    fig = Figure()
#    axis = fig.add_subplot(1, 1, 1)
#    xs = np.random.rand(100)
#    ys = np.random.rand(100)
#    axis.plot(xs, ys)
#    output = io.BytesIO()
#    FigureCanvas(fig).print_png(output)
#    return Response(output.getvalue(), mimetype='image/png')

