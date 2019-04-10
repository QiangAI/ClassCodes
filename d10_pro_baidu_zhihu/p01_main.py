import crawle.lagouapp

jobs = ['算法工程师', 'Python开发工程师', ]
for job in jobs:
    app = crawle.lagouapp.LagouApp('算法工程师')
    app.crawle()
