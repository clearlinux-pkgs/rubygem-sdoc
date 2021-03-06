#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-sdoc
Version  : 0.4.1
Release  : 8
URL      : https://rubygems.org/downloads/sdoc-0.4.1.gem
Source0  : https://rubygems.org/downloads/sdoc-0.4.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-sdoc-bin
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
Patch1: 0001-Fix-minitest-version.patch

%description
# SDoc
[![Build Status](https://travis-ci.org/zzak/sdoc.png?branch=master)](https://travis-ci.org/zzak/sdoc)

%package bin
Summary: bin components for the rubygem-sdoc package.
Group: Binaries

%description bin
bin components for the rubygem-sdoc package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n sdoc-0.4.1
gem spec %{SOURCE0} -l --ruby > rubygem-sdoc.gemspec
%patch1 -p1

%build
gem build rubygem-sdoc.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
sdoc-0.4.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/sdoc-0.4.1 && rake --trace test && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/sdoc-0.4.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/Gemfile.lock
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/bin/sdoc
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/bin/sdoc-merge
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/discover.rb
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/merge/index.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/_context.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/_head.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/class.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/file.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/index.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/apple-touch-icon.png
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/css/github.css
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/css/main.css
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/css/panel.css
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/css/reset.css
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/favicon.ico
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/i/arrows.png
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/i/results_bg.png
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/i/tree_bg.png
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/js/highlight.pack.js
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/js/jquery-1.3.2.min.js
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/js/jquery-effect.js
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/js/main.js
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/js/searchdoc.js
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/resources/panel/index.html
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/rails/search_index.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/_context.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/_head.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/class.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/file.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/index.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/apple-touch-icon.png
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/css/github.css
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/css/main.css
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/css/panel.css
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/css/reset.css
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/favicon.ico
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/i/arrows.png
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/i/results_bg.png
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/i/tree_bg.png
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/js/highlight.pack.js
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/js/jquery-1.3.2.min.js
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/js/jquery-effect.js
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/js/main.js
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/js/searchdoc.js
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/resources/panel/index.html
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/rdoc/generator/template/sdoc/search_index.rhtml
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/sdoc.rb
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/sdoc/generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/sdoc/github.rb
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/sdoc/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/sdoc/merge.rb
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/sdoc/templatable.rb
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/lib/sdoc/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/sdoc.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/spec/rdoc_generator_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/sdoc-0.4.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/sdoc-0.4.1.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/sdoc
/usr/bin/sdoc-merge
