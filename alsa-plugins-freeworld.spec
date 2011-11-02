Name:           alsa-plugins-freeworld
Version:        1.0.24
Release:        3%{?dist}
Summary:        The ALSA Plugins - freeworld version
# All packages are LGPLv2+ with the exception of samplerate which is GPLv2+
License:        LGPLv2+
Group:          System Environment/Libraries
URL:            http://www.alsa-project.org/
Source0:        ftp://ftp.alsa-project.org/pub/plugins/alsa-plugins-%{version}.tar.bz2
Source1:        a52.conf
Source2:        lavcrate.conf
Patch0:         alsa-plugins-1.0.24-backport.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  alsa-lib-devel >= 1.0.24


%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes plugins for ALSA that cannot go to Fedora.

%package a52
BuildRequires:  ffmpeg-devel
Summary:        A52 output plugin using libavcodec
Group:          System Environment/Libraries
License:        LGPLv2+
#Compatibility with some foreign packaging scheme
Provides:       alsa-plugins-a52 = %{version}-%{release}
%description a52
This plugin converts S16 linear format to A52 compressed stream and
send to an SPDIF output.  It requires libavcodec for encoding the
audio stream.

%package lavcrate
BuildRequires:  ffmpeg-devel
Summary:        Rate converter plugin using libavcodec
Group:          System Environment/Libraries
License:        LGPLv2+
#Compatibility with some foreign packaging scheme
Provides:       alsa-plugins-lavcrate = %{version}-%{release}
%description lavcrate
The plugin in rate-lavc subdirectory is an external rate converter using
libavcodec's resampler.


%prep
%setup -q -n alsa-plugins-%{version}%{?prever}
%patch0 -p1

%build
export CPPFLAGS="$(pkg-config --cflags libavcodec)"
%configure --disable-static \
  --disable-maemo-plugin \
  --disable-jack \
  --disable-pulseaudio \
  --disable-samplerate \
  --with-speex=no \
  --with-avcodec-includedir="$(pkg-config --cflags libavcodec)"

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;

# Thoses modules will be built by default but we don't want them here.
rm $RPM_BUILD_ROOT%{_libdir}/alsa-lib/libasound_module_ctl_arcam_av.so \
  $RPM_BUILD_ROOT%{_libdir}/alsa-lib/libasound_module_ctl_oss.so \
  $RPM_BUILD_ROOT%{_libdir}/alsa-lib/libasound_module_pcm_oss.so \
  $RPM_BUILD_ROOT%{_libdir}/alsa-lib/libasound_module_pcm_upmix.so \
  $RPM_BUILD_ROOT%{_libdir}/alsa-lib/libasound_module_pcm_usb_stream.so \
  $RPM_BUILD_ROOT%{_libdir}/alsa-lib/libasound_module_pcm_vdownmix.so \
  $RPM_BUILD_ROOT%{_libdir}/alsa-lib/libasound_module_pcm_speex.so || :

# Copying default configuration for a52 and lavcrate modules
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/alsa/pcm
install -pm 0644 %{SOURCE1} %{SOURCE2} \
 $RPM_BUILD_ROOT%{_sysconfdir}/alsa/pcm


%clean
rm -rf $RPM_BUILD_ROOT


%files a52
%defattr(-,root,root,-)
%doc COPYING COPYING.GPL
%doc doc/a52.txt
%dir %{_sysconfdir}/alsa/pcm
%config(noreplace) %{_sysconfdir}/alsa/pcm/a52.conf
%{_libdir}/alsa-lib/libasound_module_pcm_a52.so

%files lavcrate
%defattr(-,root,root,-)
%doc COPYING COPYING.GPL
%doc doc/lavcrate.txt
%dir %{_sysconfdir}/alsa/pcm
%config(noreplace) %{_sysconfdir}/alsa/pcm/lavcrate.conf
%{_libdir}/alsa-lib/libasound_module_rate_lavcrate.so
%{_libdir}/alsa-lib/libasound_module_rate_lavcrate_fast.so
%{_libdir}/alsa-lib/libasound_module_rate_lavcrate_faster.so
%{_libdir}/alsa-lib/libasound_module_rate_lavcrate_high.so
%{_libdir}/alsa-lib/libasound_module_rate_lavcrate_higher.so


%changelog
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

* Mon Jun 30 2009 kwizart < kwizart at gmail > - 1.0.20-3
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
