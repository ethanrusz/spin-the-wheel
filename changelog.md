# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased] - 2019-10-17
### Fixed
- Red LED now flashes while audio is playing.
- Merge errors in `changelog.md`.

## [1.4.0] - 2019-10-05
### Added
- Audio folder for easier file changing.
- Random Audio and Classic (spin the wheel) modes.

### Changed
- Made all GPIO pins variable.
- LED blink times.

### Removed
- Unused audio file `spook.mp3`.

## [1.3.0] - 2019-10-01
### Added
- Added a fifteen second exit mute.

### Fixed
- Bad indentation in `bones()`.

## [1.2.0] - 2019-09-30
### Added
- Multiprocessing for open door state.

### Changed
- Red LED no longer stops flashing while audio is playing.
- Shortened `exit()` blink duration.

### Fixed
- Cleaned up messy loops.

## [1.1.2] - 2019-09-29
### Added
- Green blink on startup.
- Missing function comments for `exit()` override.

### Changed
- Green LED no longer blinks all the time.
- Door closed reset pattern.
- Made comments more comprehensive.

## [1.1.1] - 2019-09-29
### Changed
- Better version of `bones.mp3`.

## [1.1.0] - 2019-09-29
### Added
- Kill switch in `exit()`.
- Rough version of `bones.wav`.
- Audio trigger.

### Changed
- Made `red()` more efficient.

## [1.0.1] - 2019-09-28
### Added
- Changelog template.

### Fixed
- Incorrect date in version 1.0.0.
- Broken links in `changelog.md` sources.

## [1.0.0] - 2019-09-28
### Added
- Door sensor to detect open state.
- Green and red blink functions.
- Information in `README.md`.

# Changelog Template
## [version] - yyyy-mm-dd
### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security
