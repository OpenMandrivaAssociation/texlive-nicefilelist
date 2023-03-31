Name:		texlive-nicefilelist
Epoch:		1
Version:	28527
Release:	2
Summary:	Provide \listfiles alignment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nicefilelist
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicefilelist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicefilelist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicefilelist.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends longnamefilelist, keeping separate columns
for date, version and "caption" (the caption now separately
listed). Alignment is not disturbed by short file name
extensions, such as ".fd". The package is not compatible with
longnamefilelist: users need to re-read the documentation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nicefilelist/nicefilelist.RLS
%{_texmfdistdir}/tex/latex/nicefilelist/nicefilelist.sty
%doc %{_texmfdistdir}/doc/latex/nicefilelist/README
%doc %{_texmfdistdir}/doc/latex/nicefilelist/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/latex/nicefilelist/nicefilelist.pdf
#- source
%doc %{_texmfdistdir}/source/latex/nicefilelist/empty.f
%doc %{_texmfdistdir}/source/latex/nicefilelist/nicefilelist.tex
%doc %{_texmfdistdir}/source/latex/nicefilelist/provonly.fd
%doc %{_texmfdistdir}/source/latex/nicefilelist/srcfiles.tex
%doc %{_texmfdistdir}/source/latex/nicefilelist/wrong.prv

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
