from whitenoise.storage import CompressedManifestStaticFilesStorage
from whitenoise.storage import MissingFileError


class StaticStorage(CompressedManifestStaticFilesStorage):
    """
    Keep Manifest hashing (good for production caching),
    but don't crash collectstatic if third‑party CSS references missing files.
    """
    manifest_strict = False

    def post_process(self, paths, dry_run=False, **options):
        try:
            yield from super().post_process(paths, dry_run=dry_run, **options)
        except MissingFileError:
            return