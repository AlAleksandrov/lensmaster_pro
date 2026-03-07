from whitenoise.storage import CompressedManifestStaticFilesStorage
from whitenoise.storage import MissingFileError


class StaticStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False

    def post_process(self, paths, dry_run=False, **options):
        gen = super().post_process(paths, dry_run=dry_run, **options)

        while True:
            try:
                yield next(gen)
            except StopIteration:
                break
            except MissingFileError as e:
                if options.get("verbosity", 0) >= 1:
                    print(f"WhiteNoise: skipped missing referenced static file: {e}")
                continue