from whitenoise.storage import CompressedManifestStaticFilesStorage

class CustomWhiteNoiseStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False