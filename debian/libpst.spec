Summary:            Utilities to convert Outlook .pst files to other formats
Name:               libpst
Version:            0.6.25
Release:            1%{?dist}
License:            GPLv2+
Group:              Applications/Productivity
Source:             http://www.five-ten-sg.com/%{name}/packages/%{name}-%{version}.tar.gz
BuildRoot:          %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
URL:                http://www.five-ten-sg.com/%{name}/
Requires:           ImageMagick
BuildRequires:      ImageMagick freetype-devel gd-devel libjpeg-devel zlib-devel


%description
The Libpst utilities include readpst which can convert email messages
to both mbox and MH mailbox formats, pst2ldif which can convert the
contacts to .ldif format for import into ldap databases, and pst2dii
which can convert email messages to the DII load file format used by
Summation.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%docdir %{_datadir}/doc/%{name}-%{version}
%{_datadir}/doc/%{name}-%{version}


%changelog
* Fri Jan 16 2009 Carl Byington <carl@five-ten-sg.com> - 0.6.25-1
- improve handling of content-type charset values in mime parts

* Thu Dec 11 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.24-1
- patch from Chris Eagle to build on cygwin

* Thu Dec 04 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.23-1
- bump version to avoid cvs tagging mistake in fedora

* Fri Nov 28 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.22-1
- patch from David Cuadrado to process emails with type PST_TYPE_OTHER
- base64_encode_multiple() may insert newline, needs larger malloc
- subject lines shorter than 2 bytes could segfault

* Tue Oct 21 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.21-1
- fix title bug with old schema in pst2ldif.
- also escape commas in distinguished names per rfc4514.

* Thu Oct 09 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.20-1
- add configure option --enable-dii=no to remove dependency on libgd.
- many fixes in pst2ldif by Robert Harris.
- add -D option to include deleted items, from Justin Greer
- fix from Justin Greer to add missing email headers
- fix from Justin Greer for my_stristr()
- fix for orphan children when building descriptor tree
- avoid writing uninitialized data to debug log file
- remove unreachable code
- create dummy top-of-folder descriptor if needed for corrupt pst files

* Sun Sep 14 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.19-1
- Fix base64 encoding that could create long lines.
- Initial work on a .so shared library from Bharath Acharya.

* Thu Aug 28 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.18-1
- Fixes for iconv on Mac from Justin Greer.

* Tue Aug 05 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.17-1
- More fixes for 32/64 bit portability on big endian ppc.

* Tue Aug 05 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.16-1
- Use inttypes.h for portable printing of 64 bit items.

* Wed Jul 30 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.15-1
- Patch from Robert Simpson for file handle leak in error case.
- Fix for missing length on lz decompression, bug found by Chris White.

* Sun Jun 15 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.14-1
- Fix my mistake in debian packaging.

* Fri Jun 13 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.13-1
- Patch from Robert Simpson for encryption type 2.

* Tue Jun 10 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.12-1
- Patch from Joachim Metz for debian packaging and
- fix for incorrect length on lz decompression

* Tue Jun 03 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.11-1
- Use ftello/fseeko to properly handle large files.
- Document and properly use datasize field in b5 blocks.
- Fix some MSVC compile issues and collect MSVC dependencies into one place.

* Thu May 29 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.10-1
- Patch from Robert Simpson for doubly-linked list code and arrays of unicode strings.

* Fri May 16 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.9
- Patch from Joachim Metz for 64 bit compile.
- Fix pst format documentation for 8 byte backpointers.

* Wed Mar 05 2008 Carl Byington <carl@five-ten-sg.com> - 0.6.8
- Initial version of pst2dii to convert to Summation dii load file format
- changes for Fedora packaging guidelines (#434727)

* Tue Jul 10 2007 Carl Byington <carl@five-ten-sg.com> - 0.5.5
- merge changes from Joe Nahmias version

* Sun Feb 19 2006 Carl Byington <carl@five-ten-sg.com> - 0.5.3
- initial spec file using autoconf and http://www.fedora.us/docs/rpm-packaging-guidelines.html

