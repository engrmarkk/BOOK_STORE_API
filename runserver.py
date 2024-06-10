from api import create_app
import cProfile

app = create_app()

if __name__ == '__main__':
    # profiler = cProfile.Profile()
    # profiler.enable()
    # app.run(debug=True)
    # profiler.disable()
    # profiler.print_stats(sort='time')
    cProfile.run("app.run(debug=True)", "profiler")
