from mrjob.job import MRJob


class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", ('words', len(line.split()))
        yield "lines", 1

    def reducer(self, key, values):
        if key == 'words':
            print(list(len(v) for v in values))
        else:
            yield key, sum(values)

    @classmethod
    def run(cls):
        """Entry point for running job from the command-line.

        This is also the entry point when a mapper or reducer is run
        by Hadoop Streaming.

        Does one of:

        * Print step information (:option:`--steps`). See :py:meth:`show_steps`
        * Run a mapper (:option:`--mapper`). See :py:meth:`run_mapper`
        * Run a combiner (:option:`--combiner`). See :py:meth:`run_combiner`
        * Run a reducer (:option:`--reducer`). See :py:meth:`run_reducer`
        * Run the entire job. See :py:meth:`run_job`
        """
        # load options from the command line
        mr_job = cls(args=('file.txt', ))
        mr_job.execute()


if __name__ == '__main__':
    MRWordFrequencyCount.run()
