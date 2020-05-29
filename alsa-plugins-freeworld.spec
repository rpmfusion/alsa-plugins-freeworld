Name:           alsa-plugins-freeworld
Version:        1.2.2
Release:        1%{?dist}
Summary:        The ALSA Plugins - freeworld version
# All packages are LGPLv2+ with the exception of samplerate which is GPLv2+
License:        LGPLv2+
URL:            http://www.alsa-project.org/
Source0:        ftp://ftp.alsa-project.org/pub/plugins/alsa-plugins-%{version}.tar.bz2

BuildRequires:  autoconf automake libtool
BuildRequires:  alsa-lib-devel >= 1.1.8
BuildRequires:  ffmpeg-devel

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes plugins for ALSA that cannot go to Fedora.

%package a52
Summary:        A52 output plugin using libavcodec
License:        LGPLv2+
#Compatibility with some foreign packaging scheme
Provides:       alsa-plugins-a52 = %{version}-%{release}

%description a52
This plugin converts S16 linear format to A52 compressed stream and
send to an SPDIF output.  It requires libavcodec for encoding the
audio stream.

%package lavrate
Summary:        Rate converter plugin using libavcodec
License:        LGPLv2+
#Compatibility with some foreign packaging scheme
Provides:       alsa-plugins-lavrate = %{version}-%{release}
Obsoletes:	alsa-plugins-lavcrate < 1.1.6-4

%description lavrate
The plugin uses ffmpeg audio resample library to convert audio rates.

%prep
%setup -q -n alsa-plugins-%{version}%{?prever}

%build
%configure --disable-static \
  --disable-maemo-plugin \
  --disable-jack \
  --disable-pulseaudio \
  --disable-samplerate \
  --disable-speexdsp \
  --disable-usbstream \
  --disable-arcamav \
  --disable-mix \
  --disable-oss \
  --with-speex=no

%make_build

%install
%make_install
find %buildroot -name "*.la" -exec rm {} \;

%files a52
%license COPYING COPYING.GPL
%doc doc/a52.txt
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/60-a52-encoder.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/60-a52-encoder.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_pcm_a52.so

%files lavrate
%license COPYING COPYING.GPL
%doc doc/lavrate.txt
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/10-rate-lav.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/10-rate-lav.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_rate_lavrate.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_fast.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_faster.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_high.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_higher.so


%changelog
* Fri May 29 2020 Leigh Scott <leigh123linux@gmail.com> - 1.2.2-1
- Updated to 1.2.2

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.2.1-3
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-1
- Updated to 1.2.1

* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 1.1.9-2
- Rebuild for new ffmpeg version

* Fri May 10 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.1.9-1
- Update to 1.1.9

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.1.8-1
- Update to 1.1.8

* Tue Jan 08 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.1.7-2
- Bump obsoletes

* Sat Oct 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.7-1
- Update to 1.1.7
- Drop upstreamed patches

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Jaroslav Kysela <perex@perex.cz> - 1.1.6-5
- Rename alsa-plugins-lavcrate to alsa-plugins-lavrate
- /etc/alsa/conf.d contains symlinks to /usr/share/alsa/alsa.conf.d templates

* Sat Apr 14 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.6-3
- Fix build

* Fri Apr 13 2018 Jaroslav Kysela <perex@perex.cz> - 1.1.6-2
- Use plugin config files from upstream, spec cleanups

* Fri Apr 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.1.6-1
- Update to 1.1.6

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.1.5-4
- Rebuilt for new ffmpeg snapshot

* Wed Feb 28 2018 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.5-2
- Rebuilt for ffmpeg-3.5 git

* Thu Nov 23 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.1.5-1
- Update to 1.1.5

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.1.4-1
- Update to 1.1.4

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.1.1-4
- Rebuild for ffmpeg update

* Sat Mar 18 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.1.1-2
- Rebuilt for ffmpeg-3.1.1

* Sat Jul 09 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.1.1-1
- Update to 1.1.1

* Sun Oct 25 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.0.29-1
- Update to 1.0.29

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 1.0.28-2
- Rebuilt for FFmpeg 2.4.3

* Sun Sep 28 2014 kwizart <kwizart@gmail.com> - 1.0.28-1
- Update to 1.0.28

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 1.0.27-5
- Rebuilt for ffmpeg-2.3

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 1.0.27-4
- Rebuilt for ffmpeg-2.2

* Sat Dec 07 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.27-3
- Rebuilt for FFmpeg

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.27-2
- Rebuilt for FFmpeg 2.0.x

* Sat Jun 01 2013 Daniel Ziemba <zman0900@gmail.com> - 1.0.27-1
- Update to 1.0.27

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.26-4
- Rebuilt for x264/FFmpeg

* Fri May 3 2013 Daniel Ziemba <zman0900@gmail.com> - 1.0.26-3
- Fix compatibility with libavcodec - rfbz#2648

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.26-2
- Rebuilt for FFmpeg 1.0

* Sat Sep 15 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.26-1
- Update to 1.0.26

* Tue Jul 10 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.25-3
- Fix build with gcc47

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.25-2
- Rebuilt for FFmpeg

* Thu Feb 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.25-1
- Update to 1.0.15

* Wed Nov 02 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.24-3
- Fix transition to FFmpeg-0.8 - rfbz#2011

* Fri Sep 23 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.24-2
- Rebuild for FFmpeg

* Wed Feb 02 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.24-1
- Update to 1.0.24

* Tue Oct 19 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.0.23-1
- Update to 1.0.23

* Sat Jan 16 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.0.22-1
- Update to 1.0.22

* Wed Sep  9 2009 kwizart < kwizart at gmail > - 1.0.21-1
- Update to 1.0.21

* Mon Jul  6 2009 kwizart < kwizart at gmail > - 1.0.20-4
- Correctly indent the provides
- Missing %%dir fixing ownership in -lavcrate
- Fix per package BuildRequires
- License is LGPLv2+ for all of theses plugins

* Tue Jun 30 2009 kwizart < kwizart at gmail > - 1.0.20-3
- Split a52 and lavcrate subpackages

* Wed Jun 24 2009 kwizart < kwizart at gmail > - 1.0.20-2
- Remove the plugins that can move to fedora.
- Distribute default configuration files.
- Improve description and summary

* Tue Jun 23 2009 kwizart < kwizart at gmail > - 1.0.20-1
- Initial freeworld  package.

* Fri May 8 2009 Eric Moret <eric.moret@gmail.com> - 1.0.20-1
- Updated to 1.0.20
- Added arcam-av subpackage

* Fri Apr 24 2009 Eric Moret <eric.moret@gmail.com> - 1.0.19-1
- Updated to 1.0.19
- Added Requires: alsa-utils to address #483322
- Added dir {_sysconfdir}/alsa/pcm to address #483322

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 28 2008 Eric Moret <eric.moret@gmail.com> - 1.0.18-2
- Updated to 1.0.18 final

* Thu Sep 11 2008 Jaroslav Kysela <jkysela@redhat.com> - 1.0.18-1.rc3
- Updated to 1.0.18rc3
- Added usbstream subpackage

* Mon Jul 21 2008 Jaroslav Kysela <jkysela@redhat.com> - 1.0.17-1
- Updated to 1.0.17

* Tue Mar 25 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1.0.16-4
- Kind of fix the plugins not to complain about the hints

* Wed Mar 19 2008 Eric Moret <eric.moret@gmail.com> - 1.0.16-3
- Fixing jack.conf (#435343)

* Sun Mar 09 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1.0.16-2
- Add descriptions to various PCM plugins, so they're visible in aplay -L

* Sat Mar 08 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1.0.16-1
- New upstream, dropping upstreamed patches
- Do not assert fail when pulseaudio is unavailable (#435148)

* Tue Mar 04 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1.0.15-4
- Be more heplful when there's PulseAudio trouble.
- This may save us some bogus bug reports

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.15-3
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Eric Moret <eric.moret@epita.fr> - 1.0.15-2
- Update to upstream 1.0.15 (#429249)
- Add "Requires: pulseaudio" to alsa-plugins-pulseaudio (#368891)
- Fix pulse_hw_params() when state is SND_PCM_STATE_PREPARED (#428030)
- run /sbin/ldconfig on post and postun macros

* Thu Oct 18 2007 Lennart Poettering <lpoetter@redhat.com> - 1.0.14-6
- Merge the whole /etc/alsa/pcm/pulseaudio.conf stuff into
  /etc/alsa/pulse-default.conf, because the former is practically
  always ignored, since it is not referenced for inclusion by any other
  configuration file fragment (#251943)
  The other fragments installed in /etc/alsa/pcm/ are useless, too. But
  since we are in a freeze and they are not that important, I am not fixing
  this now.

* Wed Oct 17 2007 Lennart Poettering <lpoetter@redhat.com> - 1.0.14-5
- Split pulse.conf into two, so that we can load one part from
  form /etc/alsa/alsa.conf. (#251943)

* Mon Oct 1 2007 Lennart Poettering <lpoetter@redhat.com> - 1.0.14-4
- In the pulse plugin: reflect the XRUN state back to the application.
  Makes XMMS work on top of the alsa plugin. (#307341)

* Mon Sep 24 2007 Lennart Poettering <lpoetter@redhat.com> - 1.0.14-3
- Change PulseAudio buffering defaults to more sane values

* Tue Aug 14 2007 Eric Moret <eric.moret@epita.fr> - 1.0.14-2
- Adding pulse as ALSA "default" pcm and ctl when the alsa-plugins-pulseaudio
package is installed, fixing #251943.

* Mon Jul 23 2007 Eric Moret <eric.moret@epita.fr> - 1.0.14-1
- update to upstream 1.0.14
- use configure --without-speex instead of patches to remove a52

* Tue Mar 13 2007 Matej Cepl <mcepl@redhat.com> - 1.0.14-0.3.rc2
- Really remove a52 plugin package (including changes in
  configure and configure.in)

* Thu Feb 15 2007 Eric Moret <eric.moret@epita.fr> 1.0.14-0.2.rc2
- Adding configuration files
- Removing a52 plugin package

* Wed Jan 10 2007 Eric Moret <eric.moret@epita.fr> 1.0.14-0.1.rc2
- Initial package for Fedora
